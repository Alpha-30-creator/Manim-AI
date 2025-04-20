"""Error Analyzer Agent for Manim animations.

This agent analyzes error logs from Manim animations and generates
questions to retrieve relevant documentation for fixing the errors.
"""
from typing import Dict, List
from langchain_core.prompts import ChatPromptTemplate
from models import o3_mini

class ErrorAnalyzerAgent:
    """Agent for analyzing Manim animation errors and generating questions."""
    
    def __init__(self, llm=o3_mini):
        """Initialize the Error Analyzer Agent.
        
        Args:
            llm: LangChain language model for error analysis
        """
        self.llm = llm
        
        # Define schema for structured output
        self.custom_schema = {
            "name": "ManimErrorAnalysis",
            "description": "Analyze Manim errors and generate questions for documentation retrieval",
            "parameters": {
                "type": "object",
                "properties": {
                    "error_summary": {
                        "type": "string",
                        "description": "Summary of the errors identified"
                    },
                    "questions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {"type": "string"},
                                "index": {"type": "string", "enum": ["manim-ce", "manim-voiceover"]},
                                "priority": {"type": "integer", "minimum": 1, "maximum": 5},
                                "rationale": {"type": "string"}
                            },
                            "required": ["question", "index", "priority", "rationale"]
                        }
                    }
                },
                "required": ["error_summary", "questions"]
            }
        }
        
        # Create system prompt
        self.system_prompt = """You are an expert Manim developer specializing in debugging and fixing educational animations with voiceover.

Your task is to analyze error logs from Manim animations and generate questions that will help retrieve relevant documentation for fixing the errors.

ERROR CLASSIFICATION:

1. IMPORT AND DEPENDENCY ERRORS
   • Missing or incorrect import statements
   • Improper class imports for inheritance
   • Unavailable external resources

2. INITIALIZATION ISSUES
   • Service initialization problems (Azure, GTS, etc.)
   • Class inheritance and constructor issues
   • Environment variables and credentials problems

3. ANIMATION SYNTAX ERRORS
   • Incorrect method calls and animation parameters
   • Timing and synchronization issues
   • Invalid or deprecated animation methods

4. COMPATIBILITY ISSUES
   • Object type mismatches in animations
   • Dimensional inconsistencies (2D vs 3D)
   • Improper object transformations

5. RESOURCE MANAGEMENT
   • Missing external files (SVGs, images)
   • File dependencies that need replacement

GUIDELINES:
1. Generate specific, targeted questions about Manim features needed to fix the errors
2. Separate questions between Manim core functionality (manim-ce) and voiceover-specific features (manim-voiceover)
3. Prioritize questions from 1 (highest) to 5 (lowest) based on their importance
4. Provide a brief rationale for each question explaining why it's needed
5. Focus on technical implementation details rather than content
6. Consider edge cases and potential challenges
7. Include questions about animation techniques, transitions, and voiceover synchronization

EXAMPLE QUESTIONS:
- How to properly initialize Azure speech service in Manim-voiceover? (manim-voiceover, priority: 1, rationale: Critical for voiceover functionality)
- How to fix "AttributeError: 'Scene' object has no attribute 'voiceover'" error? (manim-voiceover, priority: 1, rationale: Indicates missing VoiceoverScene inheritance)
- How to replace external SVG files with programmatically generated content? (manim-ce, priority: 3, rationale: Needed for resource independence)"""

        # Create human prompt
        self.human_prompt = """Analyze the following Manim animation error log and generate questions for retrieving relevant documentation:

ORIGINAL CODE:
{original_code}

ERROR LOG:
{error_log}

ORIGINAL SCRIPT (Optional):
{original_script}

Please generate a comprehensive list of questions that will help in fixing the errors in the animation."""

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
    
    def analyze_errors(self, 
                      original_code: str, 
                      error_log: str,
                      original_script: str = None) -> Dict:
        """Analyze Manim animation errors and generate questions.
        
        Args:
            original_code: The original Manim code with errors
            error_log: Error messages from attempting to run the code
            original_script: Optional original educational script
            
        Returns:
            Dictionary containing error summary and questions for documentation retrieval
        """
        # Prepare the prompt variables
        prompt_variables = {
            "original_code": original_code,
            "error_log": error_log,
            "original_script": original_script or "No original script provided."
        }
        
        # Generate the error analysis and questions
        response = self.structured_llm.invoke(
            self.prompt.format_messages(**prompt_variables),
        )
        
        return response 