"""
Test script for the TOC agent.

This script demonstrates using the TOC agent to generate structured
table of contents for various math topics and monitors token usage.
"""

import os
import json

from langchain_community.callbacks import get_openai_callback
import tiktoken

from agents import toc_agent
# Azure OpenAI models map to these encodings
MODEL_ENCODING_MAP = {
    "gpt-4o": "cl100k_base",
    "gpt-4o-mini": "cl100k_base",
    "o3-mini": "cl100k_base",
    "gpt-35-turbo": "cl100k_base",
    "text-embedding-ada-002": "cl100k_base"
}


def count_tokens(text, model="gpt-4o-mini"):
    """Count tokens using tiktoken.
    
    Args:
        text: The text to count tokens for
        model: The model name to use for counting
        
    Returns:
        The number of tokens in the text
    """
    # Get the encoding for the model
    encoding_name = MODEL_ENCODING_MAP.get(model, "cl100k_base")
    encoding = tiktoken.get_encoding(encoding_name)
    
    # Count tokens
    token_ids = encoding.encode(text)
    return len(token_ids)


def save_to_json(toc, filename):
    """Save the TOC to a JSON file."""
    # Create outputs directory if it doesn't exist
    output_dir = "outputs/toc_outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert Pydantic model to dict and save as JSON
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        json.dump(toc.dict(), f, indent=2)
    
    print(f"TOC saved to {filepath}")


def print_toc(toc):
    """Print the TOC in a readable format."""
    print("\n" + "="*50)
    print(f"Main Topic: {toc.main_topic}")
    print(f"Description: {toc.description}")
    print(f"Total Subtopics: {toc.total_subtopics}")
    print(f"Overall Difficulty: {toc.difficulty}")
    print(f"Target Audience: {toc.audience}")
    
    print("\nSubtopics (in learning sequence):")
    for subtopic in sorted(toc.subtopics, key=lambda x: x.order_index):
        print(f"\n{subtopic.order_index}. {subtopic.title} ({subtopic.difficulty}, {subtopic.estimated_duration} min)")
        if subtopic.prerequisites:
            print(f"   Prerequisites: {', '.join(subtopic.prerequisites)}")
        print(f"   Key Points:")
        for point in subtopic.key_points:
            print(f"     - {point}")
    print("="*50 + "\n")


def test_toc_generation():
    """Test the TOC agent with various math topics and monitor token usage."""
    
    # List of test cases: (topic, audience, filename)
    test_cases = [
        (
            "Linear Algebra Fundamentals: Vectors, matrices, transformations, and eigenvalues",
            "high school students",
            "linear_algebra_fundamentals.json"
        ),
        (
            "Calculus: Limits, derivatives, and integrals with applications to physics",
            "first-year undergraduate students",
            "calculus_basics.json"
        ),
        (
            "Probability Theory: Random variables, distributions, and expectation",
            "undergraduate statistics students",
            "probability_theory.json"
        ),
        (
            "Number Theory: Prime numbers, modular arithmetic, and cryptography applications",
            "advanced high school students",
            "number_theory.json"
        )
    ]
    
    total_tokens = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "successful_requests": 0
    }
    
    # Generate and display TOCs for each test case
    for topic, audience, filename in test_cases:
        print(f"\nGenerating TOC for: {topic}")
        print(f"Audience: {audience}")
        
        # Count tokens in the prompt (tiktoken)
        print("\nToken Usage (Tiktoken):")
        
        # Construct simplified prompt similar to what the agent would use
        prompt = f"""Generate a structured table of contents for teaching: 

{topic}

The content should be appropriate for {audience}. 
Break down the topic into logical subtopics that build upon each other in an optimal learning sequence."""
        
        prompt_tokens = count_tokens(prompt)
        print(f"  Prompt Tokens: {prompt_tokens}")
        
        # Use LangChain's callback to track token usage
        with get_openai_callback() as cb:
            try:
                # Generate the TOC
                toc = toc_agent.generate_toc(
                    topic=topic,
                    audience=audience
                )
                
                # Print and save the TOC
                print_toc(toc)
                save_to_json(toc, filename)
                
                # Convert to JSON string and count tokens
                toc_dict = toc.dict()
                toc_json = json.dumps(toc_dict)
                response_tokens = count_tokens(toc_json)
                print(f"  Response Tokens (Tiktoken): {response_tokens}")
                print(f"  Total Tokens (Tiktoken): {prompt_tokens + response_tokens}")
                
                # Print token usage for this generation (LangChain)
                print("\nToken Usage (LangChain Callback):")
                print(f"  Prompt Tokens: {cb.prompt_tokens}")
                print(f"  Completion Tokens: {cb.completion_tokens}")
                print(f"  Total Tokens: {cb.total_tokens}")
                print(f"  Cost: ${cb.total_cost:.6f}")
                
                # Update total token count using LangChain's more accurate numbers
                total_tokens["prompt_tokens"] += cb.prompt_tokens
                total_tokens["completion_tokens"] += cb.completion_tokens
                total_tokens["total_tokens"] += cb.total_tokens
                total_tokens["successful_requests"] += 1
                
            except Exception as e:
                print(f"Error generating TOC: {str(e)}")
                # Even if we get an error, add the tiktoken-counted prompt tokens
                total_tokens["prompt_tokens"] += prompt_tokens
    
    # Print total token usage across all test cases
    print("\n" + "="*50)
    print("Total Token Usage Summary:")
    print(f"  Successful Requests: {total_tokens['successful_requests']}")
    print(f"  Total Prompt Tokens: {total_tokens['prompt_tokens']}")
    print(f"  Total Completion Tokens: {total_tokens['completion_tokens']}")
    print(f"  Total Tokens: {total_tokens['total_tokens']}")
    print(f"  Average Tokens per Request: {total_tokens['total_tokens'] / max(1, total_tokens['successful_requests']):.1f}")
    print("="*50)


if __name__ == "__main__":
    print("Testing TOC Agent with Token Counting...")
    test_toc_generation()
    print("Testing complete!")
