"""Test script for the ScriptAgent.

This script demonstrates generating an educational script from a TOC subtopic.
"""
import json
import os
import tiktoken
from langchain_community.callbacks.manager import get_openai_callback

from agents import script_agent, toc_agent

# Helper function to print script information
def print_script_info(script):
    """Print key information about a generated script."""
    print(f"\n=== Script for: {script.subtopic_title} ===")
    print(f"Duration: {script.total_duration_minutes} minutes")
    print(f"Target audience: {script.target_audience}")
    print(f"Difficulty: {script.difficulty}")
    
    print("\nContent Blocks:")
    for i, block in enumerate(script.content_blocks, 1):
        print(f"  {i}. {block.type}" + (f" - {block.title}" if block.title else ""))
        print(f"     Duration: {block.duration} minutes")
        print(f"     Content (preview): {block.content[:100]}...")
    
    print("\nVisual Elements:")
    for i, element in enumerate(script.visual_elements, 1):
        print(f"  {i}. {element.description}")
        print(f"     Timing: {element.timing}")
    
    print("\nEquations:")
    for i, eq in enumerate(script.equations, 1):
        print(f"  {i}. {eq}")
    
    print("\nKey Concepts:")
    for concept in script.key_concepts:
        print(f"  - {concept}")

def count_tokens(text, model="gpt-4-0125-preview"):
    """Count tokens using tiktoken."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def save_script_to_file(script, output_dir="outputs/scripts_outputs"):
    """Save the script to a JSON file.
    
    Args:
        script: The Script object to save
        output_dir: Directory to save the script to
        
    Returns:
        Path to the saved file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Convert script to dictionary
    script_dict = script.model_dump()
    
    # Process math references in content blocks
    for block in script_dict["content_blocks"]:
        if block.get("math_references"):
            for ref_id, latex in block["math_references"].items():
                block["content"] = block["content"].replace(f"$math:{ref_id}$", latex)
    
    # Ensure proper escaping of backslashes in equations
    for i, eq in enumerate(script_dict["equations"]):
        if "\\\\" not in eq and "\\" in eq:
            script_dict["equations"][i] = eq.replace("\\", "\\\\")
    
    # Generate filename
    sanitized_title = script.subtopic_title.lower().replace(" ", "_")
    filename = os.path.join(output_dir, f"{sanitized_title}.json")
    
    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(script_dict, f, indent=2, ensure_ascii=False)
    
    return filename

def test_script_generation():
    """Test the ScriptAgent by generating a script for a math topic."""
    # Set up test parameters
    subtopic_title = "Introduction to Vectors"
    duration = 2.5
    audience = "high school students"
    difficulty = "beginner"
    prerequisites = ["Basic Algebra", "Coordinate Systems"]
    key_points = [
        "Definition of vectors",
        "Representation in 2D and 3D",
        "Vector notation",
        "Basic operations: addition and scalar multiplication"
    ]

    print(f"Generating script for: {subtopic_title}")
    
    # Use the callback to track token usage
    with get_openai_callback() as cb:
        # Generate script
        script = script_agent.generate_script(
            subtopic_title=subtopic_title,
            duration=duration,
            audience=audience,
            difficulty=difficulty,
            prerequisites=prerequisites,
            key_points=key_points
        )
        
        # Print token usage
        print(f"\nToken usage:")
        print(f"  Prompt tokens: {cb.prompt_tokens}")
        print(f"  Completion tokens: {cb.completion_tokens}")
        print(f"  Total tokens: {cb.total_tokens}")
        print(f"  Cost: ${cb.total_cost:.4f}")
    
    # Print script information
    print_script_info(script)
    
    # Save script to file
    filename = save_script_to_file(script)
    print(f"\nScript saved to: {filename}")
    
    return script

def test_script_from_toc():
    """Test generating a script from a TOC subtopic."""
    # First generate a TOC
    print("\nGenerating a sample TOC...")
    toc = toc_agent.generate_toc(
        topic="Linear Algebra: Vectors and Matrix Operations",
        audience="high school students"
    )
    
    # Get the first subtopic
    first_subtopic = toc.subtopics[0]
    print(f"\nUsing first subtopic: {first_subtopic.title}")
    
    # Generate script for this subtopic
    with get_openai_callback() as cb:
        script = script_agent.generate_script(
            subtopic_title=first_subtopic.title,
            duration=first_subtopic.estimated_duration,
            audience=toc.audience,
            difficulty=first_subtopic.difficulty,
            prerequisites=[p for p in first_subtopic.prerequisites],
            key_points=[k for k in first_subtopic.key_points]
        )
        
        # Print token usage
        print(f"\nToken usage:")
        print(f"  Prompt tokens: {cb.prompt_tokens}")
        print(f"  Completion tokens: {cb.completion_tokens}")
        print(f"  Total tokens: {cb.total_tokens}")
        print(f"  Cost: ${cb.total_cost:.4f}")
    
    # Print script information
    print_script_info(script)
    
    # Save script to file
    filename = save_script_to_file(script)
    print(f"\nScript saved to: {filename}")
    
    return script

if __name__ == "__main__":
    print("=== Testing ScriptAgent ===")
    print("\nTest 1: Generate script with direct parameters")
    test_script_generation()
    