#!/usr/bin/env python3
"""
Clean Manim documentation markdown files by removing header content.

This script processes markdown files from manim-ce and manim-voiceover directories,
removing all content from the beginning of the file up to the line containing
"Toggle table of contents sidebar" (inclusive). The cleaned files are saved to
manim-ce-cleaned and manim-voiceover-cleaned directories, preserving the original
directory structure.
"""

import os
import shutil
from pathlib import Path


def clean_markdown_file(input_file, output_file):
    """
    Clean a markdown file by removing header content.
    
    Args:
        input_file: Path to the input markdown file
        output_file: Path to save the cleaned output file
    
    Returns:
        bool: True if cleaning was successful, False if the marker line wasn't found
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for the marker line
    marker = "Toggle table of contents sidebar"
    if marker in content:
        # Find the position after the marker line
        marker_pos = content.find(marker)
        line_end_pos = content.find('\n', marker_pos)
        if line_end_pos == -1:  # If marker is on the last line
            cleaned_content = ""
        else:
            # Extract content after the marker line
            cleaned_content = content[line_end_pos + 1:].lstrip()
        
        # Write cleaned content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        return True
    else:
        # If marker not found, just copy the file as is
        shutil.copy2(input_file, output_file)
        print(f"Warning: Marker not found in {input_file}. File copied without cleaning.")
        return False


def process_directory(input_dir, output_dir):
    """
    Process all markdown files in a directory and its subdirectories.
    
    Args:
        input_dir: Input directory containing markdown files
        output_dir: Output directory for cleaned files
    
    Returns:
        tuple: (total_files, cleaned_files) counts
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    total_files = 0
    cleaned_files = 0
    
    # Walk through all files in the input directory
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith('.md'):
                total_files += 1
                
                # Calculate relative path to maintain directory structure
                rel_path = os.path.relpath(os.path.join(root, file), input_path)
                output_file = output_path / rel_path
                
                # Clean the file
                if clean_markdown_file(os.path.join(root, file), output_file):
                    cleaned_files += 1
    
    return total_files, cleaned_files


def main():
    # Base directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Input directories
    manim_ce_dir = os.path.join(base_dir, 'manim-ce')
    manim_voiceover_dir = os.path.join(base_dir, 'manim-voiceover')
    
    # Output directories
    manim_ce_cleaned_dir = os.path.join(base_dir, 'manim-ce-cleaned')
    manim_voiceover_cleaned_dir = os.path.join(base_dir, 'manim-voiceover-cleaned')
    
    # Create output directories if they don't exist
    os.makedirs(manim_ce_cleaned_dir, exist_ok=True)
    os.makedirs(manim_voiceover_cleaned_dir, exist_ok=True)
    
    # Process manim-ce documentation
    print("Processing manim-ce documentation...")
    total_ce, cleaned_ce = process_directory(manim_ce_dir, manim_ce_cleaned_dir)
    
    # Process manim-voiceover documentation
    print("Processing manim-voiceover documentation...")
    total_vo, cleaned_vo = process_directory(manim_voiceover_dir, manim_voiceover_cleaned_dir)
    
    # Print summary
    print("\nSummary:")
    print(f"manim-ce: {cleaned_ce}/{total_ce} files cleaned")
    print(f"manim-voiceover: {cleaned_vo}/{total_vo} files cleaned")
    print(f"Total: {cleaned_ce + cleaned_vo}/{total_ce + total_vo} files cleaned")


if __name__ == "__main__":
    main() 