"""Debug Agent for fixing Manim animations with errors.

This agent takes erroneous Manim code and error logs, then generates fixed code
that resolves the issues while preserving educational content.
"""
import os
from typing import Dict, Optional
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from models import o3_mini

# Load environment variables
load_dotenv()

class DebugAgent:
    """Agent for debugging and fixing Manim animations with errors."""
    
    def __init__(self, llm=o3_mini):
        """Initialize the Debug Agent.
        
        Args:
            llm: LangChain language model for code fixing
        """
        self.llm = llm
        
        # Define schema for structured output
        self.custom_schema = {
            "name": "ManimCode",
            "description": "Generate a fixed Manim animation script with proper imports and run command",
            "parameters": {
                "type": "object",
                "properties": {
                    "imports": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Required imports for the Manim script"
                    },
                    "scene_code": {
                        "type": "string",
                        "description": "Complete fixed Manim scene code"
                    },
                    "run_command": {
                        "type": "string",
                        "description": "Command to render the animation in high quality"
                    },
                    "explanation": {
                        "type": "string",
                        "description": "Explanation of the errors identified and fixes applied"
                    }
                },
                "required": ["imports", "scene_code", "run_command", "explanation"]
            }
        }
        
        # Create system prompt specifically for debugging
        self.system_prompt = """You are an expert Manim developer specializing in debugging and fixing educational animations with voiceover.

Your task is to fix Manim animation code that has errors while preserving the educational content and intent.

VISUAL MANAGEMENT (HIGHEST PRIORITY):
1. NO OVERLAPPING ELEMENTS - This is a non-negotiable requirement
2. Position each element with explicit coordinates or methods like to_edge, to_corner
3. ALWAYS use explicit buffer values (buff=0.5) for ALL positioning methods
4. Use "ONE IN, ONE OUT" rule - Remove or reposition old elements before adding new ones
5. Use absolute positioning for elements to control their exact position wherever possible
6. Make sure elements are not outside screen boundaries
7. Divide screen into appropriate non-overlapping zones (e.g., TOP for title, LEFT for text, CENTER for visuals)
8. Group related elements with VGroup for easier management and removal
9. EXPLICITLY FadeOut all elements when no longer needed - nothing vanishes without fadeout
10. Make sure that elements are not outside the screen boundaries.
11. Make sure all math expressions are written in LaTeX notation for display but spoken naturally in voiceovers.

FIX STRATEGY:
1. Preserve the educational content and intent of the original code
2. Maintain visual clarity and proper synchronization
3. Ensure smooth transitions between concepts
4. Keep the scene organized and well-structured
5. Handle perspective changes gracefully
6. Clean up unused elements
7. Respect viewer's perspective and comfort

MINIMAL INTERVENTION APPROACH:
1. Apply the smallest changes necessary to fix issues
2. Add explanatory comments for significant changes
3. Maintain code style consistency

REPLACEMENT STRATEGY:
1. When a complex animation must be replaced, substitute with a simpler equivalent
2. Ensure replacements convey the same educational concepts
3. Document replacements with clear comments

CAMERA ANGLE GUIDELINES:
When working with 3D scenes in Manim, camera angles use spherical coordinates, and the following guidelines should be followed:
1. Save camera state before 3D transitions: original_phi = self.camera.phi
2. Use phi=75° (DEGREES), theta=30° for standard 3D view but feel free to modify based on your needs
3. Reset camera when returning to 2D: self.set_camera_orientation(phi=original_phi, theta=original_theta)
4. Use begin_ambient_camera_rotation(rate=0.2) to show depth

VOICEOVER BEST PRACTICES:
When fixing code with voiceover, ensure proper synchronization:
1. Use the `with self.voiceover(text="...") as tracker:` pattern
2. Use `tracker.duration` to time animations to match the voiceover
3. Save and restore camera orientation when transitioning between 2D and 3D
4. Properly remove elements before introducing new ones to prevent overlapping
5. Chain multiple voiceovers in sequence for a complete narrative
6. Ensure animations are complete before the voiceover finishes
7. Never include LaTeX notation or symbols in voiceover text - translate mathematical expressions into spoken English

You are working with Manim CE version 0.19 and Manim-voiceover version 0.3.7.

IMPORTANT: You must explain your fixes in detail, identifying each error and describing your solution. All external files must be replaced with Manim-generated content."""

        self.human_prompt = """Fix the following Manim animation code that has errors.

ORIGINAL CODE:
{original_code}

ERROR LOG:
{error_log}

ORIGINAL SCRIPT (Optional):
{original_script}

ERROR ANALYSIS:
{error_analysis}

RELEVANT DOCUMENTATION:
{relevant_docs}

KEY CONSIDERATIONS:
- Identify and fix all errors while preserving educational intent
- Always prioritize reliability and code that will run successfully
- Replace complex problematic animations with simpler alternatives if needed
- Avoid dependencies on external files
- Ensure the animation is synchronized with voiceover
- Document any significant simplifications with explanatory comments
- Keep educational value intact even when simplifying animations

Please generate completely fixed code including necessary imports, the scene code, and the rendering command."""

        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", self.human_prompt)
        ])
        
        # Create a structured LLM
        self.structured_llm = self.llm.with_structured_output(
            schema=self.custom_schema,
            method="function_calling"
        )
    
    def fix_animation(self, 
                      original_code: str, 
                      error_log: str,
                      original_script: Optional[str] = None,
                      error_analysis: Optional[str] = None,
                      relevant_docs: Optional[str] = None) -> Dict:
        """Fix a Manim animation with errors.
        
        Args:
            original_code: The original Manim code with errors
            error_log: Error messages from attempting to run the code
            original_script: Optional original educational script
            error_analysis: Optional error analysis from ErrorAnalyzerAgent
            relevant_docs: Optional relevant documentation from DocumentRetriever
            
        Returns:
            Dictionary containing fixed imports, scene code, run command, and explanation
        """
        # Prepare the prompt variables
        prompt_variables = {
            "original_code": original_code,
            "error_log": error_log,
            "original_script": original_script or "No original script provided.",
            "error_analysis": error_analysis or "No error analysis provided.",
            "relevant_docs": relevant_docs or "No relevant documentation provided."
        }
        
        # Generate the fixed Manim code
        response = self.structured_llm.invoke(
            self.prompt.format_messages(**prompt_variables),
        )
        
        return response 