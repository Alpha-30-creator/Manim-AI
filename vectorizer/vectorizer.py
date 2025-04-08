#!/usr/bin/env python3
"""
Vectorizer for Manim documentation.

This script processes the cleaned Manim documentation files, chunks them,
extracts metadata, and uploads them to Pinecone.
"""
# Import from models
from models.azure import Embedding

# Import utility functions
from vectorizer.utils import (
    PINECONE_API_KEY,
    init_pinecone,
    prepare_vectors_for_upsert,
    save_processing_state,
    load_processing_state,
    chunk_by_headings,
    extract_metadata,
    logger
)

import os
import time
import uuid
import argparse
import sys
import json
from typing import List, Dict, Any
from pathlib import Path
from tqdm import tqdm

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Hard-coded configuration values
BATCH_SIZE = 100  # Batch size for vector uploads
EMBEDDING_BATCH_SIZE = 16  # Batch size for embedding generation


def process_file(file_path: str, source_type: str, embedding_model: Any, pinecone_index: Any) -> int:
    """
    Process a single markdown file and upload its chunks to Pinecone.
    
    Args:
        file_path: Path to the markdown file
        source_type: 'manim-ce' or 'manim-voiceover'
        embedding_model: LangChain AzureOpenAIEmbeddings model
        pinecone_index: Pinecone index to upload vectors to
        
    Returns:
        Number of chunks processed and uploaded
    """
    logger.info(f"Processing file: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chunk the content
    chunks = chunk_by_headings(content)
    logger.info(f"Created {len(chunks)} chunks")
    
    if not chunks:
        logger.warning(f"No chunks created for {file_path}")
        return 0
    
    # Extract metadata for each chunk
    metadata_list = []
    for i, chunk in enumerate(chunks):
        metadata = extract_metadata(
            chunk, file_path, source_type, i
        )
        metadata_list.append(metadata)
    
    # Generate embeddings using the AzureOpenAIEmbeddings model
    logger.info(f"Generating embeddings for {len(chunks)} chunks")
    try:
        # Process in batches to avoid rate limits
        all_embeddings = []
        
        for i in range(0, len(chunks), EMBEDDING_BATCH_SIZE):
            batch_end = min(i + EMBEDDING_BATCH_SIZE, len(chunks))
            batch_chunks = chunks[i:batch_end]
            
            # Use AzureOpenAIEmbeddings embed_documents method
            batch_embeddings = embedding_model.embed_documents(batch_chunks)
            all_embeddings.extend(batch_embeddings)
            
            # Add a small delay to avoid rate limits
            if batch_end < len(chunks):
                time.sleep(1)
        
        embeddings = all_embeddings
        
    except Exception as e:
        logger.error(f"Error generating embeddings: {str(e)}")
        raise
    
    # Generate unique IDs for chunks
    file_id = str(uuid.uuid4())[:8]
    chunk_ids = [f"{file_id}_{i}" for i in range(len(chunks))]
    
    # Prepare vectors for upsert
    batches = prepare_vectors_for_upsert(
        chunk_ids=chunk_ids,
        embeddings=embeddings,
        metadata_list=metadata_list,
        batch_size=BATCH_SIZE
    )
    
    # Upsert to the index
    logger.info(f"Upserting {len(chunks)} vectors to index")
    for i, batch in enumerate(batches):
        try:
            pinecone_index.upsert(vectors=batch)
            logger.info(f"Uploaded batch {i+1}/{len(batches)}")
        except Exception as e:
            logger.error(f"Error upserting batch {i+1}: {str(e)}")
            raise
    
    logger.info(f"Successfully processed and uploaded {len(chunks)} chunks from {file_path}")
    return len(chunks)


def process_directory(
    input_dir: str,
    source_type: str,
    embedding_model: Any,
    pinecone_index: Any,
    state_file: str,
    processed_files: List[str] = None
) -> int:
    """
    Process all markdown files in a directory and upload to Pinecone.
    
    Args:
        input_dir: Input directory containing markdown files
        source_type: 'manim-ce' or 'manim-voiceover'
        embedding_model: LangChain AzureOpenAIEmbeddings model
        pinecone_index: Pinecone index to upload vectors to
        state_file: Path to processing state file
        processed_files: List of already processed files
        
    Returns:
        Total number of chunks uploaded
    """
    if not os.path.exists(input_dir):
        logger.error(f"Directory does not exist: {input_dir}")
        return 0
    
    if processed_files is None:
        processed_files = []
    
    logger.info(f"Processing directory: {input_dir}")
    
    # Get all markdown files
    md_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    logger.info(f"Found {len(md_files)} markdown files")
    
    # Skip already processed files
    md_files = [f for f in md_files if f not in processed_files]
    logger.info(f"{len(md_files)} files remaining to process")
    
    total_chunks = 0
    
    # Process each file with a progress bar
    for file_path in tqdm(md_files, desc=f"Processing {source_type} files"):
        try:
            chunks_uploaded = process_file(file_path, source_type, embedding_model, pinecone_index)
            total_chunks += chunks_uploaded
            
            # Update processed files list and save state
            processed_files.append(file_path)
            save_processing_state(state_file, processed_files)
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}")
            # Continue with next file
    
    logger.info(f"Processed {len(md_files)} files, uploaded {total_chunks} chunks")
    return total_chunks


def main():
    """Main function to process and upload all docs to Pinecone."""
    parser = argparse.ArgumentParser(description='Upload Manim documentation to Pinecone')
    parser.add_argument('--manim-ce-dir', default='manim-ce-cleaned', help='Directory containing cleaned Manim CE docs')
    parser.add_argument('--manim-voiceover-dir', default='manim-voiceover-cleaned', help='Directory containing cleaned Manim Voiceover docs')
    parser.add_argument('--state-file', default='processing_state.json', help='Path to save processing state')
    parser.add_argument('--skip-existing', action='store_true', help='Skip already processed files')
    parser.add_argument('--only', choices=['manim-ce', 'manim-voiceover'], help='Process only one documentation source')
    
    args = parser.parse_args()
    
    # Check if Pinecone API key is available
    if not PINECONE_API_KEY:
        logger.error("PINECONE_API_KEY environment variable is not set")
        return
    
    # Get base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set paths
    manim_ce_dir = os.path.join(base_dir, args.manim_ce_dir)
    manim_voiceover_dir = os.path.join(base_dir, args.manim_voiceover_dir)
    state_file = os.path.join(base_dir, args.state_file)
    
    # Initialize embedding model
    embedding_model = Embedding.get_instance()
    
    # Initialize Pinecone for Manim CE
    logger.info("Initializing Pinecone indexes...")
    pc = init_pinecone(PINECONE_API_KEY)
    
    # Get indexes for each documentation source
    manim_ce_index = pc.Index("manim-ce")
    manim_voiceover_index = pc.Index("manim-voiceover")
    
    logger.info("Pinecone indexes initialized successfully")
    
    # Load processing state if skipping existing files
    processed_files = []
    if args.skip_existing:
        processed_files = load_processing_state(state_file)
        logger.info(f"Loaded {len(processed_files)} already processed files from state")
    
    # Process directories
    total_chunks = 0
    
    if args.only is None or args.only == 'manim-ce':
        logger.info("Processing Manim CE documentation...")
        ce_chunks = process_directory(
            manim_ce_dir, 
            'manim-ce', 
            embedding_model, 
            manim_ce_index,
            state_file,
            processed_files
        )
        total_chunks += ce_chunks
    
    if args.only is None or args.only == 'manim-voiceover':
        logger.info("Processing Manim Voiceover documentation...")
        vo_chunks = process_directory(
            manim_voiceover_dir, 
            'manim-voiceover', 
            embedding_model, 
            manim_voiceover_index,
            state_file,
            processed_files
        )
        total_chunks += vo_chunks
    
    logger.info(f"Processing complete. Total chunks uploaded: {total_chunks}")
    
    # Print final index stats
    manim_ce_stats = manim_ce_index.describe_index_stats()
    manim_vo_stats = manim_voiceover_index.describe_index_stats()
    
    logger.info(f"Manim CE index stats: {manim_ce_stats}")
    logger.info(f"Manim Voiceover index stats: {manim_vo_stats}")
    
    # Helper function to convert objects to JSON-serializable dictionaries
    def convert_to_serializable(obj):
        if hasattr(obj, '__dict__'):
            return {k: convert_to_serializable(v) for k, v in vars(obj).items()}
        elif isinstance(obj, dict):
            return {k: convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        else:
            # Convert any other types to strings
            return str(obj)
    
    # Write stats to file
    stats = {
        "timestamp": time.time(),
        "total_chunks_uploaded": total_chunks,
        "manim_ce_stats": convert_to_serializable(manim_ce_stats),
        "manim_voiceover_stats": convert_to_serializable(manim_vo_stats)
    }
    
    with open(os.path.join(base_dir, "pinecone_stats.json"), 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    
    logger.info("All documentation has been processed and uploaded to Pinecone")


if __name__ == "__main__":
    main() 