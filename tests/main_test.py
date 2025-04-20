"""Main test module for the Manim-AI project.

This module tests the end-to-end pipeline:
1. Generating Manim code from a topic and key points using code_agent
2. Reviewing the generated code using review_agent
3. Running the reviewed code
4. If errors occur, using debug_agent to fix them
5. Re-running the fixed code
6. Repeating up to 5 debug attempts

It includes safeguards to prevent excessive API calls and robust error handling.
"""

import os
import json
import time
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from langchain_community.callbacks.manager import get_openai_callback

from agents import (
    code_agent,
    debug_agent,
    question_generator,
    document_retriever,
    error_analyzer,
    review_agent
)

# Define paths
TOC_PATH = Path("outputs/toc_outputs/linear_algebra_fundamentals.json")
OUTPUT_DIR = Path("outputs/main_test_outputs")
ORIGINAL_CODE_FILE = OUTPUT_DIR / "original_code.py"
REVIEWED_CODE_FILE = OUTPUT_DIR / "reviewed_code.py"
DEBUG_CODE_PREFIX = OUTPUT_DIR / "debug_attempt_"

# Settings to control execution
MAX_DEBUG_ATTEMPTS = 5
SUBPROCESS_TIMEOUT = 1200  # 20 minutes timeout for Manim rendering
MANIM_COMMAND_TEMPLATE = "manim -qh {file} main --disable_caching"  # No preview

def ensure_directory_exists(directory):
    """Ensure the specified directory exists."""
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
    return directory

def check_manim_installed():
    """Check if Manim is properly installed and available."""
    try:
        result = subprocess.run(
            ["manim", "--version"], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Manim is installed: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Manim check returned error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Manim command not found. Please ensure Manim is installed and in your PATH.")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Manim version check timed out.")
        return False
    except Exception as e:
        print(f"❌ Error checking Manim installation: {str(e)}")
        return False

def save_code_to_file(code_dict, output_file):
    """Save the code to a Python file.
    
    Args:
        code_dict: Dictionary containing 'imports' and 'scene_code'
        output_file: Path to save the Python file
        
    Returns:
        Path to the saved file
    """
    # Create parent directories if needed
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Extract imports and scene code
    imports = code_dict.get("imports", [])
    scene_code = code_dict.get("scene_code", "")
    
    # Write to Python file
    with open(output_file, "w", encoding="utf-8") as f:
        # Write imports
        for imp in imports:
            f.write(f"{imp}\n")
        
        # Add a blank line after imports
        f.write("\n")
        
        # Write scene code
        f.write(scene_code)
    
    print(f"Code saved to: {output_file}")
    return output_file

def run_manim_code(python_file_path):
    """Run Manim code and capture output.
    
    Args:
        python_file_path: Path to the Python file to run
        
    Returns:
        Dictionary with success flag, stdout, stderr, and timeout flag
    """
    # Use subprocess to run the Manim command
    command = MANIM_COMMAND_TEMPLATE.format(file=python_file_path)
    print(f"Running command: {command}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=SUBPROCESS_TIMEOUT
        )
        
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "timeout": False
        }
    except subprocess.TimeoutExpired:
        print(f"⚠️ Execution timed out after {SUBPROCESS_TIMEOUT} seconds")
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Execution timed out after {SUBPROCESS_TIMEOUT} seconds",
            "timeout": True
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "timeout": False
        }

def extract_relevant_error(stderr_output):
    """Extract the relevant error information from stderr output.
    
    Filters out common warnings and irrelevant messages, focusing on the actual error
    traceback and message.
    
    Args:
        stderr_output: The complete stderr output
        
    Returns:
        str: The filtered error message containing only the relevant traceback
    """
    # Split the output into lines
    error_lines = stderr_output.split('\n')
    
    # List of patterns to ignore
    ignore_patterns = [
        "RuntimeWarning: Couldn't find ffmpeg",
        "'sox' is not recognized",
        "Animation ",  # Any animation progress line
        "|          |",  # Progress bar lines
        "%|",  # Progress percentage lines
        "it/s"  # Animation speed indicator
    ]
    
    # Collect relevant error lines
    relevant_lines = []
    in_traceback = False
    
    for line in error_lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Skip lines matching ignore patterns
        if any(pattern in line for pattern in ignore_patterns):
            continue
            
        # Start collecting when we see the traceback marker
        if "Traceback (most recent call last)" in line:
            in_traceback = True
            relevant_lines.append(line)
            continue
            
        # If we're in the traceback, collect lines
        if in_traceback:
            relevant_lines.append(line)
            
        # If we find an actual error (typically starts with an exception name), include it
        if any(err in line for err in ["Error:", "Exception:", "AttributeError:", "TypeError:", "ValueError:", "NameError:"]):
            if not in_traceback:
                relevant_lines.append(line)
    
    return '\n'.join(relevant_lines)

def save_error_log(error_text, attempt_number, filtered=False):
    """Save error output to a log file.
    
    Args:
        error_text: The error text to save
        attempt_number: The debug attempt number (0 for original)
        filtered: Whether this is the filtered error log
        
    Returns:
        Path to the saved error log
    """
    if attempt_number == 0:
        suffix = "filtered_error.log" if filtered else "original_error.log"
        error_file = OUTPUT_DIR / suffix
    else:
        suffix = f"debug_attempt_{attempt_number}_{'filtered' if filtered else 'full'}.log"
        error_file = OUTPUT_DIR / suffix
    
    try:
        with open(error_file, "w", encoding="utf-8") as f:
            f.write(error_text)
        
        print(f"Error log saved to: {error_file}")
        return error_file
    except Exception as e:
        print(f"❌ Failed to save error log: {str(e)}")
        return None

def log_execution_summary(execution_log):
    """Save the execution summary to a JSON file."""
    log_file = OUTPUT_DIR / "execution_summary.json"
    
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(execution_log, f, indent=2)
        
        print(f"Execution summary saved to: {log_file}")
        return log_file
    except Exception as e:
        print(f"❌ Failed to save execution summary: {str(e)}")
        return None

def main():
    """Run the main testing pipeline."""
    print("\n=== Starting Manim-AI End-to-End Test ===\n")
    
    # Ensure output directory exists
    ensure_directory_exists(OUTPUT_DIR)
    
    # Check if Manim is installed
    if not check_manim_installed():
        print("❌ Cannot proceed without Manim. Exiting.")
        return
    
    # Verify TOC file exists
    if not TOC_PATH.exists():
        print(f"❌ TOC file not found: {TOC_PATH}")
        return
    
    # Load the TOC data
    try:
        with open(TOC_PATH, "r") as f:
            toc_data = json.load(f)
            print(f"Loaded TOC from {TOC_PATH}")
    except Exception as e:
        print(f"❌ Failed to load TOC file: {str(e)}")
        return
    
    # Select a subtopic (for testing, we'll use the first one)
    subtopic = toc_data["subtopics"][6]
    print(f"Selected subtopic: {subtopic['title']}")
    
    # Create execution log
    execution_log = {
        "timestamp": datetime.now().isoformat(),
        "toc_path": str(TOC_PATH),
        "subtopic": subtopic["title"],
        "debug_attempts": [],
        "token_usage": {},
        "final_result": "not_started"
    }
    
    try:
        # Start tracking token usage
        with get_openai_callback() as cb:
            # STEP 1: Generate initial code
            print("\n📝 STEP 1: Generating Manim code from subtopic...")
            start_time = time.time()
            
            # Generate questions for documentation
            questions_response = question_generator.generate_questions(
                topic=subtopic["title"],
                topic_description=subtopic["description"],
                duration=subtopic["estimated_duration"]
            )
            
            # Extract the questions list from the response
            questions = questions_response["questions"]
            print(f"Generated {len(questions)} questions for documentation")
            
            # Retrieve relevant documentation
            documentation = document_retriever.retrieve_docs(questions)
            print("Retrieved relevant documentation")
            
            # Generate animation code with documentation context
            animation_code = code_agent.generate_animation(
                topic=subtopic["title"],
                topic_description=subtopic["description"],
                duration=subtopic["estimated_duration"],
                relevant_docs=documentation
            )
            generation_time = time.time() - start_time
            
            execution_log["generation_time"] = generation_time
            execution_log["questions_generated"] = len(questions)
            
            print(f"✅ Code generated in {generation_time:.2f} seconds")
            
            # Save the generated code
            code_file = save_code_to_file(animation_code, ORIGINAL_CODE_FILE)
            
            # STEP 2: Review the generated code
            print("\n🔍 STEP 2: Reviewing generated code...")
            review_start_time = time.time()
            
            # Read the generated code
            try:
                with open(code_file, "r", encoding="utf-8") as f:
                    code_text = f.read()
            except Exception as e:
                print(f"❌ Failed to read code file: {str(e)}")
                execution_log["final_result"] = "file_read_error"
                log_execution_summary(execution_log)
                return
            
            # Review the code
            review_result = review_agent.review_animation(
                original_code=code_text,
                topic=subtopic["title"],
                topic_description=subtopic["description"],
                duration=subtopic["estimated_duration"],
                relevant_docs=documentation
            )
            review_time = time.time() - review_start_time
            
            # Log review time
            execution_log["review_time"] = review_time
            
            print(f"✅ Code review completed in {review_time:.2f} seconds")
            
            # Save the reviewed code
            reviewed_code_file = save_code_to_file(review_result, REVIEWED_CODE_FILE)
            
            # STEP 3: Run the reviewed code
            print("\n🚀 STEP 3: Running reviewed code...")
            result = run_manim_code(reviewed_code_file)
            
            # Check if the run was successful
            if result["success"]:
                print("✅ Reviewed code executed successfully! No debugging needed.")
                execution_log["final_result"] = "review_success"
                
                # Print the run command for reference
                run_command = MANIM_COMMAND_TEMPLATE.format(file=reviewed_code_file)
                print(f"\n📋 Run command: {run_command}")
            else:
                print("❌ Reviewed code execution failed. Starting debug process.")
                
                # Save the error log
                error_log = save_error_log(result["stderr"], 0)
                
                # Initialize debugging variables
                debug_attempt = 0
                current_code_file = reviewed_code_file
                try:
                    with open(reviewed_code_file, "r", encoding="utf-8") as f:
                        current_code_text = f.read()
                except Exception as e:
                    print(f"❌ Failed to read code file: {str(e)}")
                    execution_log["final_result"] = "file_read_error"
                    log_execution_summary(execution_log)
                    return
                
                final_success = False
                
                # STEP 4-5: Debug loop
                while debug_attempt < MAX_DEBUG_ATTEMPTS:
                    debug_attempt += 1
                    print(f"\n🔧 Debug Attempt {debug_attempt}/{MAX_DEBUG_ATTEMPTS}...")
                    
                    # Skip debugging if timeout occurred (to save API calls)
                    if result["timeout"]:
                        print("⚠️ Skipping debugging due to timeout - likely a resource issue, not a code error")
                        execution_log["debug_attempts"].append({
                            "attempt": debug_attempt,
                            "result": "timeout",
                            "error": result["stderr"]
                        })
                        execution_log["final_result"] = "timeout"
                        break
                    
                    # Extract relevant error information
                    filtered_error = extract_relevant_error(result["stderr"])
                    
                    # Save both full and filtered error logs
                    error_log = save_error_log(result["stderr"], debug_attempt)
                    filtered_log = save_error_log(filtered_error, debug_attempt, filtered=True)
                    
                    # Analyze the error using filtered error log
                    error_analysis = error_analyzer.analyze_errors(
                        original_code=current_code_text,
                        error_log=filtered_error,
                        original_script=json.dumps({
                            "topic": subtopic["title"],
                            "key_points": subtopic["description"],
                            "duration": subtopic["estimated_duration"]
                        })
                    )
                    print("✅ Error analysis completed")
                    
                    # Extract the questions list directly from the error analysis
                    error_questions = error_analysis["questions"]
                    print(f"Generated {len(error_questions)} questions for error resolution")
                    
                    # Retrieve relevant documentation for error
                    error_documentation = document_retriever.retrieve_docs(error_questions)
                    print("Retrieved error-specific documentation")
                    
                    # Attempt to fix the code using filtered error log
                    fixed_code = debug_agent.fix_animation(
                        original_code=current_code_text,
                        error_log=filtered_error,
                        original_script=json.dumps({
                            "topic": subtopic["title"],
                            "key_points": subtopic["description"],
                            "duration": subtopic["estimated_duration"]
                        }),
                        error_analysis=error_analysis["error_summary"],
                        relevant_docs=error_documentation
                    )
                    
                    # Save the fixed code
                    debug_code_file = DEBUG_CODE_PREFIX.with_name(f"debug_attempt_{debug_attempt}.py")
                    save_code_to_file(fixed_code, debug_code_file)
                    
                    # Run the fixed code
                    result = run_manim_code(debug_code_file)
                    
                    # Log the debug attempt
                    debug_log = {
                        "attempt": debug_attempt,
                        "error_analysis": error_analysis["error_summary"],
                        "questions_generated": len(error_questions),
                        "success": result["success"]
                    }
                    execution_log["debug_attempts"].append(debug_log)
                    
                    if result["success"]:
                        print("✅ Code fixed successfully!")
                        final_success = True
                        execution_log["final_result"] = "debug_success"
                        
                        # Print the run command for reference
                        run_command = MANIM_COMMAND_TEMPLATE.format(file=debug_code_file)
                        print(f"\n📋 Run command: {run_command}")
                        break
                    else:
                        print("❌ Fix attempt failed. Saving error log...")
                        save_error_log(result["stderr"], debug_attempt)
                        current_code_file = debug_code_file
                        current_code_text = fixed_code
                
                if not final_success:
                    print("❌ All debug attempts failed.")
                    execution_log["final_result"] = "debug_failed"
            
            # Log token usage
            execution_log["token_usage"] = {
                "total_tokens": cb.total_tokens,
                "prompt_tokens": cb.prompt_tokens,
                "completion_tokens": cb.completion_tokens,
                "total_cost": cb.total_cost
            }
            
            # Save execution summary
            log_execution_summary(execution_log)
            
            print("\n=== Manim-AI End-to-End Test Complete ===")
            print(f"Final result: {execution_log['final_result']}")
            print(f"Total tokens used: {cb.total_tokens}")
            print(f"Total cost: ${cb.total_cost:.4f}")
            
    except Exception as e:
        print(f"❌ Fatal error in main test: {str(e)}")
        execution_log["final_result"] = "fatal_error"
        execution_log["error"] = str(e)
        log_execution_summary(execution_log)
        raise

if __name__ == "__main__":
    main() 