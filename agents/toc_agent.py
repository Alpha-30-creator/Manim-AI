"""TOC Agent for generating structured table of contents for educational videos.

This agent takes a topic and generates a structured TOC with proper learning sequence,
ensuring topics are in the correct order for optimal learning progression.
"""
import json
import re
from typing import List, Literal

from pydantic import BaseModel, Field, validator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class SubTopic(BaseModel):
    """Model representing a subtopic within the main educational topic."""
    
    title: str = Field(description="Title of the subtopic")
    order_index: int = Field(description="Order in which this subtopic should be taught/watched")
    estimated_duration: float = Field(description="Estimated video duration in minutes")
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(description="Difficulty level of the subtopic")
    prerequisites: List[str] = Field(default_factory=list, description="List of prerequisite subtopics that should be watched before this one")
    description: str = Field(description="Detailed description of the mathematical content to be covered, including key concepts, equations, properties, and examples")
    
    @classmethod
    @validator('estimated_duration')
    def duration_in_range(cls, v):
        """Validate that the video duration is within reasonable limits."""
        if v < 1.0 or v > 5.0:
            raise ValueError('Video duration should be between 1 and 5 minutes')
        return v

class Topic(BaseModel):
    """Model representing the main educational topic with its subtopics."""
    
    main_topic: str = Field(description="Main topic title")
    description: str = Field(description="Brief description of the topic")
    total_subtopics: int = Field(description="Total number of subtopics")
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(description="Overall difficulty level")
    audience: str = Field(description="Target audience for this content")
    subtopics: List[SubTopic] = Field(description="List of subtopics in proper learning sequence")
    
    @classmethod
    @validator('subtopics')
    def validate_order(cls, subtopics):
        """Validate that subtopics are in the correct order and prerequisites are consistent."""
        # Check if order_index values are sequential and start from 1
        order_indices = [st.order_index for st in subtopics]
        if sorted(order_indices) != list(range(1, len(subtopics) + 1)):
            raise ValueError("Subtopic order_index must be sequential and start from 1")
        
        # Check for prerequisite consistency
        available_topics = []
        for st in sorted(subtopics, key=lambda x: x.order_index):
            for prereq in st.prerequisites:
                if prereq not in available_topics and prereq != st.title:
                    raise ValueError(f"Prerequisite '{prereq}' for '{st.title}' appears after or doesn't exist")
            available_topics.append(st.title)
            
        # Check that duration values aren't all the same
        durations = [st.estimated_duration for st in subtopics]
        if len(set(durations)) == 1 and len(durations) > 1:
            raise ValueError("All subtopics have the same duration. Durations should vary based on complexity.")
            
        return subtopics


class TOCAgent:
    """Agent for generating structured table of contents for educational videos."""
    
    def __init__(
        self, 
        llm,
        max_subtopics: int = 10,
        target_video_duration: float = 2.5,
        max_depth: int = 2
    ):
        """Initialize the TOC Agent.
        
        Args:
            llm: LangChain language model to use
            max_subtopics: Maximum number of subtopics per main topic
            target_video_duration: Target duration in minutes per subtopic video
            max_depth: Maximum depth of topic hierarchy
        """
        self.llm = llm
        self.max_subtopics = max_subtopics
        self.target_duration = target_video_duration
        self.max_depth = max_depth
        
        # Create a system prompt template
        self.system_prompt = """You are an expert educational content designer specializing in mathematics. 
Your task is to create a structured table of contents for a series of educational videos.

IMPORTANT GUIDELINES:
1. Organize topics in the CORRECT LEARNING SEQUENCE, where each topic builds on previous ones
2. TIME MANAGEMENT IS CRITICAL - carefully structure subtopics with these time constraints:
   - Simple introductory topics: 1-2 minutes
   - Moderate complexity topics: 2-3 minutes
   - Complex topics with deeper analysis: 3-5 minutes
   - NEVER exceed 5 minutes for any subtopic
   - NEVER use the same duration for all subtopics
3. Design subtopic content specifically to fit within the estimated time:
   - More complex topics should have more concise descriptions to fit time constraints
   - Simpler topics can cover more detailed explanations in less time
   - Carefully consider what can realistically be taught in the allotted minutes
4. Limit to a maximum of {max_subtopics} subtopics, but use fewer if the topic doesn't need that many
5. For each subtopic, include:
   - A detailed description covering:
     * Key mathematical concepts and definitions
     * Essential equations and formulas
     * Mathematical properties and theorems
     * Step-by-step procedures for calculations
     * Relationships to other mathematical concepts
     * Common misconceptions or pitfalls
     * Example problems and solutions
   - Prerequisites from earlier subtopics
   - Difficulty level (beginner/intermediate/advanced)
   - Realistic estimated duration in MINUTES based on content complexity

The topics MUST be in proper pedagogical order where:
- Earlier topics provide necessary foundations for later topics
- A student should be able to progress through the topics sequentially
- Each subtopic should depend only on concepts covered in previous subtopics
- Prerequisites should only refer to topics that appear earlier in the sequence
- Duration must be proportional to complexity and scope of content
- Similar complexity topics should have similar durations
- Break down complex topics into smaller subtopics rather than assigning longer durations"""

        self.human_prompt = """Generate a structured table of contents for teaching: 

{topic}

The content should be appropriate for {audience}. 
Break down the topic into logical subtopics that build upon each other in an optimal learning sequence.
Remember that each subtopic must be teachable within 1-5 minutes, with the specific duration matching the complexity of the material."""

        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", self.human_prompt)
        ])
        
        # Define custom schema manually to avoid Pydantic _SpecialForm issues
        self.custom_schema = {
            "name": "Topic",
            "description": "Generate a structured educational topic with proper learning sequence",
            "parameters": {
                "type": "object",
                "properties": {
                    "main_topic": {
                        "type": "string",
                        "description": "Main topic title"
                    },
                    "description": {
                        "type": "string",
                        "description": "Brief description of the topic"
                    },
                    "total_subtopics": {
                        "type": "integer",
                        "description": "Total number of subtopics"
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["beginner", "intermediate", "advanced"],
                        "description": "Overall difficulty level"
                    },
                    "audience": {
                        "type": "string",
                        "description": "Target audience for this content"
                    },
                    "subtopics": {
                        "type": "array",
                        "description": "List of subtopics in proper learning sequence. Each subtopic must be carefully designed to fit within its specified time duration (1-5 minutes). The content scope, detail level, and complexity should all be proportional to the time allocated.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Title of the subtopic"
                                },
                                "order_index": {
                                    "type": "integer",
                                    "description": "Order in which this subtopic should be taught/watched"
                                },
                                "estimated_duration": {
                                    "type": "number",
                                    "description": "Estimated video duration in minutes - this is a critical factor in designing the subtopic content. Duration must be realistic for teaching the content and should vary based on complexity (1-2 min for simple topics, 2-3 min for moderate, 3-5 min for complex).",
                                    "minimum": 1.0,
                                    "maximum": 5.0
                                },
                                "difficulty": {
                                    "type": "string",
                                    "enum": ["beginner", "intermediate", "advanced"],
                                    "description": "Difficulty level of the subtopic"
                                },
                                "prerequisites": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    },
                                    "description": "List of prerequisite subtopics that should be watched before this one"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Detailed description of the mathematical content to be covered, including key concepts, equations, properties, and examples"
                                }
                            },
                            "required": ["title", "order_index", "estimated_duration", "difficulty", "description"]
                        }
                    }
                },
                "required": ["main_topic", "description", "total_subtopics", "difficulty", "audience", "subtopics"]
            }
        }
        
        # Create a structured LLM that outputs using our custom schema instead of relying on Pydantic model conversion
        self.structured_llm = self.llm.with_structured_output(
            schema=self.custom_schema,
            method="function_calling"
        )
        
    def generate_toc(
        self,
        topic: str,
        audience: str = "high school students"
    ) -> Topic:
        """Generate a table of contents for the given topic (synchronous version).
        
        Args:
            topic: The main topic to generate TOC for (provide a detailed description)
            audience: Target audience e.g high school students, college students, etc.
            
        Returns:
            A structured Topic object with subtopics in proper learning sequence
        """
        # Prepare the prompt variables
        prompt_variables = {
            "topic": topic,
            "audience": audience,
            "target_duration": self.target_duration,
            "max_subtopics": self.max_subtopics,
        }
        
        # Generate the TOC using the structured LLM
        try:
            # Get the raw response from the LLM
            response = self.structured_llm.invoke(self.prompt.format_messages(**prompt_variables))
            
            # If response is already a Topic object, return it
            if isinstance(response, Topic):
                return response
                
            # If it's a dictionary, convert it to a Topic object
            if isinstance(response, dict):
                return Topic(**response)
                
            # Otherwise, handle other response formats (like structured_output)
            if hasattr(response, 'parsed'):
                return Topic(**response.parsed)
                
            raise ValueError(f"Unexpected response format: {type(response)}")
        except Exception as e:
            raise ValueError(f"Failed to generate TOC: {str(e)}")
    
    async def generate_toc_async(
        self,
        topic: str,
        audience: str = "high school students"
    ) -> Topic:
        """Generate a table of contents for the given topic (async version).
        
        Args:
            topic: The main topic to generate TOC for (provide a detailed description)
            audience: Target audience e.g high school students, college students, etc.
            
        Returns:
            A structured Topic object with subtopics in proper learning sequence
        """
        # Prepare the prompt variables
        prompt_variables = {
            "topic": topic,
            "audience": audience,
            "target_duration": self.target_duration,
            "max_subtopics": self.max_subtopics,
        }
        
        # Generate the TOC using the structured LLM (async)
        try:
            # Get the raw response from the LLM
            response = await self.structured_llm.ainvoke(self.prompt.format_messages(**prompt_variables))
            
            # If response is already a Topic object, return it
            if isinstance(response, Topic):
                return response
                
            # If it's a dictionary, convert it to a Topic object
            if isinstance(response, dict):
                return Topic(**response)
                
            # Otherwise, handle other response formats (like structured_output)
            if hasattr(response, 'parsed'):
                return Topic(**response.parsed)
                
            raise ValueError(f"Unexpected response format: {type(response)}")
        except Exception as e:
            raise ValueError(f"Failed to generate TOC: {str(e)}")
