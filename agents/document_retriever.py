"""Document Retriever for Manim animations.

This module provides functionality to retrieve and format documentation
based on questions about Manim functionality.
"""
from typing import Dict, List
from langchain_pinecone import PineconeVectorStore



class DocumentRetriever:
    """Class for retrieving and formatting documentation based on questions."""
    
    def __init__(self, manim_ce_vectorstore: PineconeVectorStore, manim_voiceover_vectorstore: PineconeVectorStore):
        """Initialize the Document Retriever.
        
        Args:
            manim_ce_vectorstore: Vector store for Manim CE documentation
            manim_voiceover_vectorstore: Vector store for Manim Voiceover documentation
        """
        self.manim_ce_vectorstore = manim_ce_vectorstore
        self.manim_voiceover_vectorstore = manim_voiceover_vectorstore
    
    def retrieve_docs(self, questions: List[Dict], k: int = 3) -> str:
        """Retrieve and format documentation for all questions.
        
        Args:
            questions: List of questions with their index, priority, and rationale
            k: Number of results to return for each question
            
        Returns:
            Formatted string with relevant documentation snippets
        """
        # Sort questions by priority (1 is highest)
        sorted_questions = sorted(questions, key=lambda q: q["priority"])
        
        # Retrieve documentation for each question
        formatted_docs = []
        for question in sorted_questions:
            query = question["question"]
            index_name = question["index"]
            priority = question["priority"]
            rationale = question["rationale"]
            
            # Select the appropriate vector store based on the index_name
            if index_name == "manim-ce":
                vectorstore = self.manim_ce_vectorstore
            elif index_name == "manim-voiceover":
                vectorstore = self.manim_voiceover_vectorstore
            else:
                formatted_docs.append(f"Error: Unknown index name '{index_name}'. Use 'manim-ce' or 'manim-voiceover'.")
                continue
            
            try:
                # Use similarity_search_with_score to get relevance scores
                results = vectorstore.similarity_search_with_score(query, k=k)
                
                # Format results for this question
                question_docs = [f"QUESTION: {query} (Priority: {priority}, Rationale: {rationale})"]
                
                for i, (doc, score) in enumerate(results):
                    # Extract metadata if available
                    metadata = getattr(doc, 'metadata', {})
                    title = metadata.get('title', 'Untitled')
                    doc_type = metadata.get('doc_type', 'documentation')
                    file_path = metadata.get('file_path', 'unknown')
                    
                    # Format the document with metadata and relevance score
                    formatted_doc = f"RESULT {i+1}: {title} ({doc_type}) - {file_path} (relevance: {score:.2f})\n\n"
                    formatted_doc += "CONTENT:\n" + doc.page_content
                    question_docs.append(formatted_doc)
                
                formatted_docs.append("\n\n".join(question_docs))
                
            except Exception as e:
                formatted_docs.append(f"Error retrieving documentation for question '{query}': {str(e)}")
        
        # Join all formatted docs with a separator
        return "\n\n---\n\n".join(formatted_docs) 