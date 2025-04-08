#!/usr/bin/env python3
"""
Utility functions for Manim documentation vectorization.

This module contains utility functions for working with Pinecone,
managing state for the vectorization process, metadata extraction,
chunking, and logging.
"""

import os
import json
import logging
import re
import uuid
from typing import List, Dict, Any, Tuple, Optional
from dotenv import load_dotenv
import pinecone


# Setup logging
logger = logging.getLogger('manim_docs_vectorizer')
logger.setLevel(logging.INFO)

# Create console handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)


# Load environment variables from .env file
load_dotenv()

# Get Pinecone API key
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("Missing required environment variable: PINECONE_API_KEY")


def init_pinecone(api_key: str) -> pinecone.Pinecone:
    """
    Initialize Pinecone client
    
    Args:
        api_key: Pinecone API key
        
    Returns:
        Initialized Pinecone client
    """
    pc = pinecone.Pinecone(
        api_key=api_key,
        environment="aws",  
        region="us-east-1"           
    )
    return pc


def prepare_vectors_for_upsert(chunk_ids: List[str], embeddings: List[List[float]], 
                              metadata_list: List[Dict[str, Any]], batch_size: int = 100) -> List[List[Dict]]:
    """
    Prepare vectors for Pinecone upsert.
    
    Args:
        chunk_ids: List of chunk IDs
        embeddings: List of embedding vectors
        metadata_list: List of metadata dictionaries
        batch_size: Size of batches for upserting
        
    Returns:
        List of batches, where each batch is a list of vectors
    """
    vectors = []
    
    for i, (chunk_id, embedding, metadata) in enumerate(zip(chunk_ids, embeddings, metadata_list)):
        vector = {
            "id": chunk_id,
            "values": embedding,
            "metadata": metadata
        }
        vectors.append(vector)
    
    # Split into batches
    batches = []
    for i in range(0, len(vectors), batch_size):
        batch = vectors[i:i + batch_size]
        batches.append(batch)
    
    return batches


def save_processing_state(state_file: str, processed_files: List[str]) -> None:
    """
    Save the list of processed files to a state file.
    
    Args:
        state_file: Path to the state file
        processed_files: List of processed file paths
    """
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump({"processed_files": processed_files}, f, indent=2)
        logger.info(f"Saved processing state with {len(processed_files)} processed files")


def load_processing_state(state_file: str) -> List[str]:
    """
    Load the list of processed files from a state file.
    
    Args:
        state_file: Path to the state file
        
    Returns:
        List of processed file paths
    """
    if not os.path.exists(state_file):
        logger.info("No processing state file found, starting fresh")
        return []
    
    try:
        with open(state_file, 'r', encoding='utf-8') as f:
            state = json.load(f)
            processed_files = state.get("processed_files", [])
            logger.info(f"Loaded processing state with {len(processed_files)} processed files")
            return processed_files
    except Exception as e:
        logger.error(f"Error loading processing state: {str(e)}")
        return [] 


# Chunking functions

def chunk_by_headings(text: str, min_chunk_size: int = 300, max_chunk_size: int = 2048) -> List[str]:
    """
    Split text into chunks based on headings.
    Ensures code blocks stay intact.
    
    Args:
        text: The text to split
        min_chunk_size: Minimum size of a chunk in characters
        max_chunk_size: Maximum size of a chunk in characters
        
    Returns:
        List of text chunks
    """
    # First, identify all code blocks to avoid splitting them
    code_block_pattern = r'```(?:.+?)?\n(?:.+?)\n```'
    code_blocks = [(m.start(), m.end()) for m in re.finditer(code_block_pattern, text, re.DOTALL)]
    
    # Find all headings and their positions
    heading_pattern = r'^(#+)\s+(.+?)(?:\s*\[\¶\]|\s*\[#\]|\s*$)'
    headings = [(m.start(), len(m.group(1)), m.group(2).strip()) 
               for m in re.finditer(heading_pattern, text, re.MULTILINE)]
    
    # Add document end as a final "heading position"
    headings.append((len(text), 0, "END_OF_DOCUMENT"))
    
    chunks = []
    
    # Process each section between headings
    for i in range(len(headings) - 1):
        start_pos, level, heading = headings[i]
        end_pos = headings[i + 1][0]
        
        section_text = text[start_pos:end_pos].strip()
        
        # Skip empty sections
        if not section_text:
            continue
            
        # If section is too long, split it further
        if len(section_text) > max_chunk_size:
            # Find safe splitting points that don't break code blocks
            subsections = _split_large_section(section_text, code_blocks, min_chunk_size, max_chunk_size)
            chunks.extend(subsections)
        else:
            chunks.append(section_text)
    
    # Post-process: merge very small chunks with neighbors
    merged_chunks = _merge_small_chunks(chunks, min_chunk_size)
    
    # Final validation to ensure no code blocks are broken
    validated_chunks = _validate_code_blocks(merged_chunks)
    
    return validated_chunks

def _split_large_section(text: str, code_blocks: List[Tuple[int, int]], min_chunk_size: int, max_chunk_size: int) -> List[str]:
    """
    Split a large section into smaller chunks without breaking code blocks.
    
    Args:
        text: The text to split
        code_blocks: List of code block positions (start, end)
        min_chunk_size: Minimum size of a chunk in characters
        max_chunk_size: Maximum size of a chunk in characters
        
    Returns:
        List of text chunks
    """
    # Find code block positions within this section
    section_start = text.find(text)
    section_code_blocks = [
        (start - section_start, end - section_start) 
        for start, end in code_blocks 
        if section_start <= start < section_start + len(text)
    ]
    
    chunks = []
    start_idx = 0
    
    while start_idx < len(text):
        # Find a good end position around max_chunk_size
        end_idx = min(start_idx + max_chunk_size, len(text))
        
        # Check if we're in the middle of a code block
        in_code_block = False
        for block_start, block_end in section_code_blocks:
            # If this chunk would split a code block, extend to include the whole block
            if start_idx <= block_start < end_idx and end_idx < block_end:
                end_idx = block_end
                in_code_block = True
                break
            # If we're completely within a code block, use the entire block
            elif block_start <= start_idx and end_idx <= block_end:
                end_idx = block_end
                in_code_block = True
                break
        
        if not in_code_block:
            # Find the last paragraph break before end_idx
            last_break = text.rfind('\n\n', start_idx, end_idx)
            
            if last_break != -1 and last_break > start_idx + min_chunk_size:
                end_idx = last_break
        
        # Extract chunk and add to list
        chunk_text = text[start_idx:end_idx].strip()
        if chunk_text:
            chunks.append(chunk_text)
        
        start_idx = end_idx
    
    return chunks

def _merge_small_chunks(chunks: List[str], min_chunk_size: int) -> List[str]:
    """
    Merge very small chunks with their neighbors.
    
    Args:
        chunks: List of text chunks
        min_chunk_size: Minimum size of a chunk in characters
        
    Returns:
        List of merged text chunks
    """
    if not chunks:
        return []
        
    result = [chunks[0]]
    
    for chunk in chunks[1:]:
        # If current chunk is too small, merge with the previous one
        if len(chunk) < min_chunk_size and result:
            result[-1] = result[-1] + "\n\n" + chunk
        # If previous chunk is still small, merge current into it
        elif result and len(result[-1]) < min_chunk_size:
            result[-1] = result[-1] + "\n\n" + chunk
        else:
            result.append(chunk)
    
    return result
    
def _validate_code_blocks(chunks: List[str]) -> List[str]:
    """
    Ensure no code blocks are broken across chunks.
    
    Args:
        chunks: List of text chunks
        
    Returns:
        List of validated text chunks
    """
    validated = []
    current = None
    
    for chunk in chunks:
        # Count code block markers
        code_markers = chunk.count('```')
        
        # If odd number of markers, this chunk has broken code blocks
        if code_markers % 2 != 0:
            if current is None:
                # Start of a broken block
                current = chunk
            else:
                # End of a broken block, merge and add
                merged = current + "\n\n" + chunk
                validated.append(merged)
                current = None
        else:
            # Even number of markers, chunk is self-contained
            if current is not None:
                # We have a pending broken chunk but this one is complete
                # This is unexpected - add both separately
                validated.append(current)
                validated.append(chunk)
                current = None
            else:
                validated.append(chunk)
    
    # If we have a leftover chunk with unclosed code block, add it anyway
    if current is not None:
        validated.append(current)
        
    return validated


# Metadata extraction functions

def extract_metadata(chunk_text: str, file_path: str, source: str, chunk_index: int) -> Dict[str, Any]:
    """
    Extract metadata from a chunk of text.
    
    Args:
        chunk_text: The chunk text
        file_path: Original file path
        source: 'manim-ce' or 'manim-voiceover'
        chunk_index: Position of chunk in the original document
        
    Returns:
        Dictionary of metadata
    """
    # Extract document type from path
    doc_type = get_doc_type(file_path)
    
    # Extract title from first heading or filename if no heading
    title = extract_title(chunk_text, file_path)
    
    # Extract parent headings
    parent_headings = extract_parent_headings(file_path, chunk_text)
    
    # Check if contains code and extract code elements
    has_code_blocks = has_code(chunk_text)
    code_elements = extract_code_elements(chunk_text) if has_code_blocks else []
    
    # Process file path to store only the relative part from vectorizer dir
    # Extract just the part after manim-ce-cleaned or manim-voiceover-cleaned
    if "manim-ce-cleaned" in file_path:
        relative_path = file_path.split("manim-ce-cleaned")[-1].strip("/\\")
    elif "manim-voiceover-cleaned" in file_path:
        relative_path = file_path.split("manim-voiceover-cleaned")[-1].strip("/\\")
    else:
        # Fallback to basename if path doesn't contain expected directories
        relative_path = os.path.basename(file_path)
    
    return {
        "source": source,
        "doc_type": doc_type,
        "title": title,
        "file_path": relative_path,
        "parent_headings": parent_headings,
        "contains_code": has_code_blocks,
        "code_elements": code_elements,
        "chunk_index": chunk_index,
        "text": chunk_text  # Include the text for vector retrieval
    }

def get_doc_type(file_path: str) -> str:
    """
    Determine document type from file path.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Document type (reference, tutorial, example, api, or documentation)
    """
    path_str = str(file_path).lower()
    
    if "reference" in path_str:
        return "reference"
    elif "tutorial" in path_str or "quickstart" in path_str:
        return "tutorial"
    elif "example" in path_str:
        return "example"
    elif "api" in path_str:
        return "api"
    else:
        return "documentation"

def extract_title(text: str, file_path: str = None) -> str:
    """
    Extract title from the first heading in the text or filename if no heading.
    
    Args:
        text: The text to extract title from
        file_path: Original file path (optional)
        
    Returns:
        Extracted title
    """
    heading_match = re.search(r'^(#+)\s+(.+?)(?:\s*\[\¶\]|\s*\[#\]|\s*$)', text, re.MULTILINE)
    if heading_match:
        # Clean the title of any URLs or references
        title = heading_match.group(2).strip()
        # Remove markdown links [text](url)
        title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
        # Remove any remaining [#] or [¶] reference marks
        title = re.sub(r'\s*\[.*?\]', '', title)
        return title.strip()
    
    # If no heading found, derive title from filename
    if file_path:
        filename = os.path.basename(file_path)
        
        # Remove extension
        filename = os.path.splitext(filename)[0]
        
        # Clean up common prefixes
        for prefix in ["docs_manim_community_en_stable_", "voiceover_manim_community_en_stable_"]:
            if filename.startswith(prefix):
                filename = filename[len(prefix):]
        
        # Remove html suffix if present
        if filename.endswith('_html'):
            filename = filename[:-5]
            
        # Replace underscores with spaces and capitalize
        title = filename.replace('_', ' ').title()
        return title
        
    # Last resort fallback
    return "Untitled Section"

def extract_parent_headings(file_path: str, text: str) -> List[str]:
    """
    Determine parent headings from file structure and content.
    
    Args:
        file_path: Path to the file
        text: The text to extract parent headings from
        
    Returns:
        List of parent headings
    """
    file_name = os.path.basename(file_path)
    
    # Extract all headings and their levels
    headings = []
    heading_pattern = r'^(#+)\s+(.+?)(?:\s*\[\¶\]|\s*\[#\]|\s*$)'
    
    for match in re.finditer(heading_pattern, text, re.MULTILINE):
        level = len(match.group(1))
        # Clean title similarly to extract_title
        title = match.group(2).strip()
        title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
        title = re.sub(r'\s*\[.*?\]', '', title)
        headings.append((level, title.strip()))
    
    # If we have headings, process parent-child relationship
    if headings:
        # Get first heading as the title
        title_level = headings[0][0]
        
        # Find parent headings (must be higher in hierarchy than title)
        parent_headings = []
        
        # Track smallest heading level seen so far to maintain hierarchy
        current_parent_level = title_level
        
        for level, title in headings[1:]:
            # If we find a heading higher in hierarchy than current parent
            if level < current_parent_level:
                parent_headings.append(title)
                current_parent_level = level
        
        if parent_headings:
            return parent_headings
    
    # Fallback to path-based heading extraction
    parts = file_name.split('_')
    if len(parts) > 1:
        path_part = parts[0].replace('docs_manim_community_en_stable_', '')
        path_part = path_part.replace('voiceover_manim_community_en_stable_', '')
        return [path_part]
        
    return []

def has_code(text: str) -> bool:
    """
    Check if text contains code blocks.
    
    Args:
        text: The text to check
        
    Returns:
        True if the text contains code blocks, False otherwise
    """
    return '```' in text

def extract_code_elements(text: str) -> List[str]:
    """
    Extract class and function names from code blocks.
    
    Args:
        text: The text to extract code elements from
        
    Returns:
        List of extracted code elements
    """
    # Find all code blocks with improved regex
    code_blocks = re.findall(r'```(?:python)?\n(.*?)\n```', text, re.DOTALL)
    
    elements = []
    # Extract class and function definitions
    class_pattern = r'class\s+(\w+)'
    func_pattern = r'def\s+(\w+)'
    import_pattern = r'from\s+\S+\s+import\s+([^()\n]+)'
    object_pattern = r'(\w+)\s*=\s*\w+\('  # Captures object creation
    
    for block in code_blocks:
        elements.extend(re.findall(class_pattern, block))
        elements.extend(re.findall(func_pattern, block))
        
        # Extract imported objects
        for imports in re.findall(import_pattern, block):
            for item in imports.split(','):
                clean_item = item.strip()
                if clean_item and clean_item != '*':
                    elements.append(clean_item)
                    
        # Add created objects
        elements.extend(re.findall(object_pattern, block))
    
    # Look for code elements in inline code
    inline_code = re.findall(r'`([^`]+)`', text)
    elements.extend([code for code in inline_code if re.match(r'^[A-Za-z][A-Za-z0-9_]*$', code)])
    
    # Remove duplicates, keywords, and sort
    python_keywords = {'self', 'True', 'False', 'None', 'and', 'or', 'if', 'else', 'elif',
                       'for', 'while', 'in', 'is', 'not', 'try', 'except', 'finally', 
                       'with', 'as', 'def', 'class', 'return', 'import', 'from'}
    
    filtered_elements = [e for e in elements if e not in python_keywords]
    
    return sorted(list(set(filtered_elements))) 