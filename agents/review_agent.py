"""Review Agent for Manim animations.

This agent reviews Manim code for quality, coherence, and adherence to guidelines.
It analyzes aspects like topic alignment, visual clarity, transitions, and camera angles.
"""
from typing import Dict, List, Optional
from langchain_core.prompts import ChatPromptTemplate
from models import o3_mini

class ReviewAgent:
    """Agent for reviewing Manim animation code for quality and adherence to guidelines."""
    
    def __init__(self, llm=o3_mini):
        """Initialize the Review Agent.
        
        Args:
            llm: LangChain language model for code review
        """
        self.llm = llm
        
        # Define schema for structured output
        self.custom_schema = {
            "name": "ManimCodeReview",
            "description": "Review Manim code for quality, coherence, and adherence to guidelines",
            "parameters": {
                "type": "object",
                "properties": {
                    "imports": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of import statements"
                    },
                    "scene_code": {
                        "type": "string",
                        "description": "The scene code"
                    },
                    "run_command": {
                        "type": "string",
                        "description": "Command to render the animation in high quality"
                    }
                },
                "required": ["imports", "scene_code", "run_command"]
            }
        }
        
        # Create system prompt
        self.system_prompt = """You are an expert Manim developer specializing in reviewing educational animations with voiceover.

Your task is to review Manim code for quality control, focusing on the following critical aspects:

VISUAL CLARITY QUALITY CONTROL (HIGHEST PRIORITY):
1. REJECT ANY CODE with overlapping elements(elements are text, visuals, formulas, etc) - this is non-negotiable
2. Verify ALL elements use explicit positioning with buffer parameters
3. Check that EVERY element has a clearly defined position
4. Ensure text is never placed where it will overlap with visuals
5. Verify sufficient margins around all elements (minimum 0.3 units)
7. Verify coordinate systems are appropriately scaled for their content
8. Check that all text has appropriate font sizes (24-36 for labels, 36-48 for titles)
9. Ensure related elements are grouped using VGroup for management
10. Verify positions use absolute coordinates or explicit methods (to_edge, to_corner)
11. Make sure to use proper latex notation for mathematical expressions
12. Any animations used should be relevant to the topic and not just for the sake of it
13. Make sure that elements are not outside the screen boundaries.

ELEMENT LIFECYCLE VERIFICATION (CRITICAL):
1. Verify EVERY element is explicitly removed when no longer needed
2. Check that FadeOut is used for ALL element removals
3. Confirm elements are grouped logically for removal
4. Ensure scene is cleaned up before new concepts are introduced
5. Verify fadeouts have appropriate timing (typically tracker.duration * 0.2)
6. Check the "ONE IN, ONE OUT" rule: when new content enters a region, old content exits
7. Ensure ALL elements have a clear lifecycle (creation, use, removal)

LAYOUT BALANCE VERIFICATION (CRITICAL):
1. Check screen is divided into logical zones based on scene (for example: title, main content, supporting) and these zones are not overlapping
2. Verify elements are distributed appropriately across the screen
3. Ensure visual hierarchy is clear and logical
4. Confirm text and visuals are properly separated. THEY SHOULD NOT OVERLAP.
5. Check that related elements are positioned near each other

CAMERA MANAGEMENT (FOR 3D SCENES):
1. Verify camera state is saved before 3D transitions
2. Check camera is reset when returning to 2D
3. Ensure appropriate camera angles for content (phi=75°, theta=30° for standard view)
4. Verify smooth transitions between different perspectives

VOICEOVER SYNCHRONIZATION:
1. Verify consistent use of "with self.voiceover(text='...') as tracker:"
2. Check animations use run_time=tracker.duration or proportional fractions
3. Ensure animations complete slightly before voiceover ends
4. Verify voiceover text matches what's being shown on screen

EDUCATIONAL EFFECTIVENESS:
1. Check each concept is properly introduced before use
2. Verify technical terms are clearly defined
3. Ensure content progresses from simple to complex
4. Check all key points from the topic description are covered

IMPORTANT NOTES:
1. Focus ONLY on code logic and educational content - assume syntax is correct
2. If you find no issues, return the original code unchanged
3. Your output should only include the imports, scene code, and run command
4. Fix ALL visual clarity and element spacing issues - this is the highest priority
5. Verify all elements are properly cleaned up when no longer needed"""

        # Create human prompt
        self.human_prompt = """Review the following Manim animation code for quality, coherence, and adherence to guidelines:

ORIGINAL CODE:
{original_code}

TOPIC INFORMATION:
Topic: {topic}
Description: {topic_description}
Duration: {duration} minutes

RELEVANT DOCUMENTATION:
{relevant_docs}

Please review the code and provide an improved version if needed. If no issues are found, return the original code unchanged."""

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
    
    def review_animation(self, 
                        original_code: str, 
                        topic: str,
                        topic_description: str,
                        duration: int,
                        relevant_docs: str = "") -> Dict:
        """Review Manim animation code for quality and adherence to guidelines.
        
        Args:
            original_code: The Manim code to review
            topic: The educational topic of the animation
            topic_description: Description of the topic and key points
            duration: Target duration in minutes
            relevant_docs: Relevant documentation to help with implementation
            
        Returns:
            Dictionary containing imports, scene code, and run command
        """
        # Prepare the prompt variables
        prompt_variables = {
            "original_code": original_code,
            "topic": topic,
            "topic_description": topic_description,
            "duration": duration,
            "relevant_docs": relevant_docs
        }
        
        # Generate the code review
        response = self.structured_llm.invoke(
            self.prompt.format_messages(**prompt_variables),
        )
        
        return response 