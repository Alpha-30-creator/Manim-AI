"""Question Generator Agent for Manim animations.

This agent generates a list of necessary questions about Manim functionality
that need to be answered before creating an animation.
"""
from typing import Dict, List
from langchain_core.prompts import ChatPromptTemplate
from models import o3_mini

class QuestionGeneratorAgent:
    """Agent for generating necessary questions about Manim functionality."""
    
    def __init__(self, llm=o3_mini):
        """Initialize the Question Generator Agent.
        
        Args:
            llm: LangChain language model for question generation
        """
        self.llm = llm
        
        # Define schema for structured output
        self.custom_schema = {
            "name": "ManimQuestions",
            "description": "Generate list of necessary questions about Manim functionality",
            "parameters": {
                "type": "object",
                "properties": {
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
                "required": ["questions", "index"]
            }
        }
        
        # Create system prompt
        self.system_prompt = """You are an expert Manim developer specializing in educational animations with voiceover.

Your task is to generate a list of necessary questions about Manim functionality that need to be answered before creating an animation.

GUIDELINES:
1. Generate specific, targeted questions about Manim features needed for the animation
2. Separate questions between Manim core functionality (manim-ce) and voiceover-specific features (manim-voiceover)
3. Prioritize questions from 1 (highest) to 5 (lowest) based on their importance
4. Provide a brief rationale for each question explaining why it's needed
5. Focus on technical implementation details rather than content
6. Consider edge cases and potential challenges
7. Include questions about animation techniques, transitions, and voiceover synchronization

EXAMPLE QUESTIONS:
- How to create a 3D scene with labeled axes? (manim-ce, priority: 3, rationale: Needed for visualizing 3D concepts)
- How to synchronize animations with specific words in the voiceover? (manim-voiceover, priority: 2, rationale: Critical for educational clarity)
- How to create smooth transitions between different mathematical concepts? (manim-ce, priority: 2, rationale: Ensures flow between key points)"""

        # Create human prompt
        self.human_prompt = """Generate a list of necessary questions about Manim functionality for the following topic and topic description:

TOPIC:
{topic}

TOPIC DESCRIPTION:
{topic_description}

TARGET DURATION:
{duration} minutes

Please generate a comprehensive list of questions that will help in creating an effective educational animation."""

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
    
    def generate_questions(self, topic: str, topic_description: str, duration: int) -> Dict:
        """Generate a list of necessary questions about Manim functionality.
        
        Args:
            topic: The educational topic to animate
            topic_description: Description of the topic to cover in the animation
            duration: Target duration of the video in minutes
            
        Returns:
            Dictionary containing a list of questions with their index, priority, and rationale
        """
        # Prepare the prompt variables
        prompt_variables = {
            "topic": topic,
            "topic_description": topic_description,
            "duration": duration
        }
        
        # Generate the questions
        response = self.structured_llm.invoke(
            self.prompt.format_messages(**prompt_variables),
        )
        
        return response 