"""Script Agent for generating educational content scripts.

This agent takes a subtopic from a Table of Contents and generates a detailed
educational script with appropriate content blocks and visual elements.
"""
from typing import List, Dict, Any, Optional, Literal

from pydantic import BaseModel, Field, validator
from langchain_core.prompts import ChatPromptTemplate

class VisualElement(BaseModel):
    """Model representing a visual element to be displayed during the video."""
    description: str = Field(description="Brief description of what this visual represents")
    timing: str = Field(description="When this visual should appear in the content flow")
    details: str = Field(description="Detailed description of what should be visualized")

class ContentBlock(BaseModel):
    """Model representing a flexible content block in the educational script."""
    type: str = Field(description="Type of content block (e.g., concept_introduction, example, geometric_interpretation)")
    title: Optional[str] = Field(None, description="Optional title for this content block")
    content: str = Field(description="The educational content")
    duration: float = Field(description="Estimated duration in minutes")
    math_references: Optional[Dict[str, str]] = Field(None, description="Math references used in this content")

class Script(BaseModel):
    """Model representing an educational script for a mathematical subtopic."""
    subtopic_title: str = Field(description="Title of the subtopic")
    total_duration_minutes: float = Field(description="Total duration in minutes")
    target_audience: str = Field(description="Target audience for this script")
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(description="Difficulty level of the content")
    
    # Core content - flexible structure based on topic needs
    content_blocks: List[ContentBlock] = Field(description="Flexible list of content blocks")
    
    # Visual guidance - optional
    visual_elements: Optional[List[VisualElement]] = Field(default_factory=list, description="Descriptions of visual elements to be shown")
    
    # Mathematical elements - optional
    equations: Optional[List[str]] = Field(default_factory=list, description="Key equations to be displayed")
    key_concepts: Optional[List[str]] = Field(default_factory=list, description="Key mathematical concepts covered")
    
    @classmethod
    @validator('total_duration_minutes')
    def validate_duration(cls, v, values):
        """Validate that the duration is reasonable."""
        if v <= 0 or v > 10:
            raise ValueError("Duration must be positive and not exceed 10 minutes")
        return v
    
    @classmethod
    @validator('content_blocks')
    def validate_content_blocks(cls, blocks, values):
        """Validate that the content blocks' durations sum to total duration."""
        if not blocks:
            raise ValueError("At least one content block is required")
        
        total_duration = sum(block.duration for block in blocks)
        expected_duration = values.get('total_duration_minutes', 0)
        
        # Allow a small margin of error (0.1 minutes)
        if abs(total_duration - expected_duration) > 0.1:
            raise ValueError(f"Content blocks duration ({total_duration}) doesn't match total duration ({expected_duration})")
        
        return blocks

class ScriptAgent:
    """Agent for generating educational scripts from TOC subtopics."""
    
    def __init__(
        self, 
        llm
    ):
        """Initialize the Script Agent.
        
        Args:
            llm: LangChain language model to use
        """
        self.llm = llm
        
        # Create a system prompt template
        self.system_prompt = """You are an expert mathematics educator specializing in creating educational scripts.
Your task is to create a detailed educational script for a mathematics subtopic that will be turned into a video.

IMPORTANT GUIDELINES:
1. Adapt your teaching approach to the specific mathematical concept - choose the most effective method
   for conveying this particular topic (examples, visualizations, step-by-step processes, etc.)
2. Create appropriate content blocks that best teach this concept within the given time constraint
3. Be precise about what should be visualized, focusing on WHAT to show, not HOW to implement it
4. Use LaTeX for all mathematical expressions (with proper escaping: \\\\, not \\)
5. Target the specified audience level and difficulty
6. Ensure all content fits within the specified duration
7. Focus on educational clarity - make complex concepts accessible
8. Include proper mathematical notation and terminology

Consider these teaching approaches and use the most appropriate ones:
- Conceptual explanation (for abstract or foundational topics)
- Visual/geometric interpretation (for topics that benefit from spatial understanding)
- Step-by-step procedures (for algorithmic or process-based topics)
- Examples and counterexamples (for topics where specific cases illustrate the concept)
- Real-world applications (for topics where practical usage aids understanding)
- Historical context (where the development of the concept is illuminating)

Remember that different mathematical topics require different teaching approaches. Choose content blocks that
best suit the specific topic you're teaching while respecting the time constraints."""

        self.human_prompt = """Create an educational script for the following mathematical subtopic:

SUBTOPIC: {subtopic_title}
AUDIENCE: {audience}
DIFFICULTY: {difficulty}
DURATION: {duration} minutes
PREREQUISITES: {prerequisites}
KEY POINTS: {key_points}

Design appropriate content blocks that effectively teach this topic in the allocated time.
Include visual elements that would help illustrate the concepts.
Provide any key equations using LaTeX notation."""

        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", self.human_prompt)
        ])
        
        # Define custom schema for the structured output
        self.custom_schema = {
            "name": "Script",
            "description": "Generate an educational script for a mathematical subtopic",
            "parameters": {
                "type": "object",
                "properties": {
                    "subtopic_title": {
                        "type": "string",
                        "description": "Title of the subtopic"
                    },
                    "total_duration_minutes": {
                        "type": "number",
                        "description": "Total duration in minutes"
                    },
                    "target_audience": {
                        "type": "string",
                        "description": "Target audience for this script"
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"],
                        "description": "Difficulty level of the content"
                    },
                    "content_blocks": {
                        "type": "array",
                        "description": "Flexible list of content blocks",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "description": "Type of content block"
                                },
                                "title": {
                                    "type": "string",
                                    "description": "Optional title for this content block"
                                },
                                "content": {
                                    "type": "string",
                                    "description": "The educational content"
                                },
                                "duration": {
                                    "type": "number",
                                    "description": "Estimated duration in minutes"
                                },
                                "math_references": {
                                    "type": "object",
                                    "description": "Math references used in this content"
                                }
                            },
                            "required": ["type", "content", "duration"]
                        }
                    },
                    "visual_elements": {
                        "type": "array",
                        "description": "Descriptions of visual elements to be shown",
                        "items": {
                            "type": "object",
                            "properties": {
                                "description": {
                                    "type": "string",
                                    "description": "Brief description of what this visual represents"
                                },
                                "timing": {
                                    "type": "string",
                                    "description": "When this visual should appear in the content flow"
                                },
                                "details": {
                                    "type": "string",
                                    "description": "Detailed description of what should be visualized"
                                }
                            },
                            "required": ["description", "timing", "details"]
                        }
                    },
                    "equations": {
                        "type": "array",
                        "description": "Key equations to be displayed",
                        "items": {
                            "type": "string"
                        }
                    },
                    "key_concepts": {
                        "type": "array",
                        "description": "Key mathematical concepts covered",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "subtopic_title", "total_duration_minutes", "target_audience", 
                    "difficulty", "content_blocks"
                ]
            }
        }
        
        # Create a structured LLM
        self.structured_llm = self.llm.with_structured_output(
            schema=self.custom_schema,
            method="function_calling"
        )
    
    def generate_script(
        self,
        subtopic_title: str,
        duration: float,
        audience: str,
        difficulty: str,
        prerequisites: List[str],
        key_points: List[str]
    ) -> Script:
        """Generate an educational script for a mathematical subtopic.
        
        Args:
            subtopic_title: Title of the subtopic
            duration: Duration in minutes
            audience: Target audience
            difficulty: Difficulty level (beginner, intermediate, advanced)
            prerequisites: List of prerequisite topics
            key_points: Key points to cover in this subtopic
            
        Returns:
            A Script object with the generated educational content
        """
        # Prepare the prompt variables
        prompt_variables = {
            "subtopic_title": subtopic_title,
            "duration": duration,
            "audience": audience,
            "difficulty": difficulty,
            "prerequisites": ", ".join(prerequisites),
            "key_points": ", ".join(key_points)
        }
        
        # Generate the script using the structured LLM
        response = self.structured_llm.invoke(self.prompt.format_messages(**prompt_variables))
        
        # If response is already a Script object, return it
        if isinstance(response, Script):
            return response
            
        # If it's a dictionary, convert it to a Script object
        if isinstance(response, dict):
            return Script(**response)
            
        # Otherwise, handle other response formats
        if hasattr(response, 'parsed'):
            return Script(**response.parsed)
            
        raise ValueError(f"Unexpected response format: {type(response)}")
