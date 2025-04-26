"""Code Agent for generating Manim animations with voiceover.

This agent takes a topic, key points, and relevant documentation to generate
a Manim animation with synchronized voiceover using Azure TTS service.
"""
import os
from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from models import o3_mini

# Load environment variables
load_dotenv()

AZURE_SPEECH_KEY = os.getenv("AZURE_SUBSCRIPTION_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SERVICE_REGION")

class CodeAgent:
    """Agent for generating Manim animations from educational topics."""
    
    def __init__(self, llm=o3_mini, azure_speech_key=AZURE_SPEECH_KEY, azure_speech_region=AZURE_SPEECH_REGION):
        """Initialize the Code Agent.
        
        Args:
            llm: LangChain language model (o3-mini) for code generation
            azure_speech_key: Azure Speech key
            azure_speech_region: Azure Speech region
        """
        self.llm = llm
        self.azure_speech_key = azure_speech_key
        self.azure_speech_region = azure_speech_region          
        
        # Define schema for structured output
        self.custom_schema = {
            "name": "ManimCode",
            "description": "Generate a Manim animation script with proper imports and run command",
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
                        "description": "Complete Manim scene code"
                    },
                    "run_command": {
                        "type": "string",
                        "description": "Command to render the animation in high quality"
                    }
                },
                "required": ["imports", "scene_code", "run_command"]
            }
        }
        
        # Create developer prompt (using developer role instead of system)
        self.system_prompt = f"""You are an expert Manim developer specializing in educational animations with voiceover, creating high-quality animated videos for beginners with no prior knowledge.

CORE REQUIREMENTS:
1. Create a single Manim scene named "main" that inherits from VoiceoverScene
2. Initialize Azure service with subscription_key = {self.azure_speech_key} and region = {self.azure_speech_region}
3. Structure code with clear section comments
4. Use proper latex notation for mathematical expressions

VISUAL MANAGEMENT (HIGHEST PRIORITY):
1. NO OVERLAPPING ELEMENTS - Position each element with explicit coordinates or methods
2. Use "ONE IN, ONE OUT" - Remove or reposition old elements before adding new ones
3. ALWAYS use explicit buffer values (buff=0.5) for ALL positioning methods
4. Make sure that elements are not outside the screen boundaries.
5. For better visual management, divide screen into approproiate zones based on the specific scene for example: TOP (title), LEFT (text), CENTER (visuals), RIGHT (supporting formulas) (THESE ZONES SHOULD NOT OVERLAP)
6. Group related elements with VGroup for easier management and removal
7. EXPLICITLY FadeOut all elements when no longer needed - nothing vanishes without fadeout

EDUCATIONAL STRUCTURE:
1. Start with clear introduction of the topic
2. Present concepts incrementally, building complexity gradually to take viewer from basic to advanced concepts while remaining inside scope of the topic (which human will provide).
3. Pause at appropriate intervals to allow the viewer to process the information before introducing a new concept.
4. Use examples to illustrate abstract concepts
5. Use natural language for voiceover text - avoid complex math expressions in speech. Never include LaTeX notation or symbols in voiceover text. See MATH IN VOICEOVERS section below for detailed examples.

VOICEOVER SYNCHRONIZATION:
1. Use "with self.voiceover(text='...') as tracker:" for all animations
2. Set run_time=tracker.duration or fractions (e.g., tracker.duration * 0.6)
3. Always include visuals with voiceovers - never have speech without visual elements
4. Allocate time for fadeouts (typically tracker.duration * 0.2)

MATH IN VOICEOVERS (CRITICAL):
- ALWAYS translate mathematical expressions into spoken English
- Mathematical expressions should be written in LaTeX for display but spoken naturally in voiceovers.

CAMERA GUIDELINES (FOR 3D):
1. Save camera state before 3D transitions: original_phi = self.camera.phi
2. Use phi=75° (DEGREES), theta=30° for standard 3D view but feel free to modify based on your needs
3. Reset camera when returning to 2D: self.set_camera_orientation(phi=original_phi, theta=original_theta)
4. Use begin_ambient_camera_rotation(rate=0.2) to show depth

EXAMPLE CODE:
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class Main(ThreeDScene, VoiceoverScene):
    def construct(self):
        # Set up the Azure speech service
        self.set_speech_service(
            AzureService(
                subscription_key="{self.azure_speech_key}",
                region="{self.azure_speech_region}"
            )
        )
        
        # Create initial 2D scene elements
        title = Text("Dimension Transitions", font_size=40)
        title.to_edge(UP)
        
        circle = Circle(radius=2, color=BLUE)
        
        # First voiceover: Introduce and show title
        with self.voiceover(text="Welcome to this demonstration of transitioning between 2D and 3D scenes in Manim.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Second voiceover: Show circle
        with self.voiceover(text="Let's start with a simple 2D circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        # Save the original camera state
        original_phi = self.camera.phi
        original_theta = self.camera.theta
        
        # Third voiceover: Transition to 3D
        with self.voiceover(text="Now, watch as we transition into the third dimension.") as tracker:
            # Remove 2D elements before transitioning to 3D
            self.play(
                FadeOut(title),
                FadeOut(circle),
                run_time=tracker.duration * 0.3
            )
            
            # Set up 3D scene
            axes = ThreeDAxes()
            sphere = Surface(
                lambda u, v: np.array([
                    1.5 * np.cos(u) * np.cos(v),
                    1.5 * np.cos(u) * np.sin(v),
                    1.5 * np.sin(u)
                ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2]
            )
            sphere.set_fill(BLUE_E, opacity=0.7)
            
            # Move to 3D perspective
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.play(
                Create(axes),
                Create(sphere),
                run_time=tracker.duration * 0.7
            )
        
        # Fourth voiceover: Rotate the 3D scene
        with self.voiceover(text="This three-dimensional sphere demonstrates proper perspective handling in Manim.") as tracker:
            self.begin_ambient_camera_rotation(rate=0.2)
            self.wait(tracker.duration * 0.8)
            self.stop_ambient_camera_rotation()
        
        # Fifth voiceover: Transition back to 2D
        with self.voiceover(text="Now, let's return to two dimensions.") as tracker:
            # Remove previous 3D elements before returning to 2D
            self.play(
                FadeOut(axes),
                FadeOut(sphere),
                run_time=tracker.duration * 0.4
            )
            
            # Reset camera to original orientation
            self.set_camera_orientation(
                phi=original_phi,
                theta=original_theta
            )
            
            # Create new 2D elements
            new_title = Text("Back to 2D", font_size=40)
            new_title.to_edge(UP)
            square = Square(side_length=4, color=RED)
            
            # Introduce new 2D elements
            self.play(
                Write(new_title),
                run_time=tracker.duration * 0.3
            )
            self.play(
                Create(square),
                run_time=tracker.duration * 0.3
            )
        
        # Add explanation text
        explanation = Text("Smooth transitions between dimensions", font_size=24)
        explanation.next_to(new_title, DOWN, buff=0.5)
        
        # Final voiceover
        with self.voiceover(
            text="By carefully managing camera orientation and element transitions, we can achieve smooth transitions between 2D and 3D scenes.",
            subcaption="Clean Transitions are Key!"
        ) as tracker:
            self.play(
                Write(explanation),
                run_time=tracker.duration * 0.5
            )
            self.wait(tracker.duration * 0.3)
            # Clean up all elements at the end
            self.play(
                FadeOut(new_title),
                FadeOut(explanation),
                FadeOut(square),
                run_time=tracker.duration * 0.2
            )
```
Best Practices demonstrated in this example:
1. Proper voiceover synchronization with animations
2. Proper camera angle for 3D scenes
3. Proper element positioning with buffers
4. Proper element cleanup and removal with FadeOut

DOCUMENTATION:
You are working with Manim CE version 0.19 and Manim-voiceover version 0.3.7.
Use the provided documentation alongside your own knowledge to create an effective animation."""

        self.human_prompt = """Generate a Manim animation with voiceover for the following topic and topic description:

TOPIC:
{topic}

TOPIC DESCRIPTION:
{topic_description}

TARGET DURATION:
{duration} minutes

RELEVANT DOCUMENTATION:
{relevant_docs}

Please generate complete code including necessary imports and the rendering command."""

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
        
    def generate_animation(self, topic: str, topic_description: str, duration: int, relevant_docs: str) -> Dict:
        """Generate a Manim animation from a topic and key points.
        
        Args:
            topic: The educational topic to animate
            topic_description: Description of the topic to cover in the animation
            duration: Target duration of the video in minutes
            relevant_docs: Relevant documentation to help with implementation
            
        Returns:
            Dictionary containing imports, scene code, and run command
        """
        # Prepare the prompt variables
        prompt_variables = {
            "topic": topic,
            "topic_description": topic_description,
            "duration": duration,
            "relevant_docs": relevant_docs
        }
        
        # Generate the Manim code
        # Using max_completion_tokens=100000 as per Azure OpenAI documentation
        response = self.structured_llm.invoke(
            self.prompt.format_messages(**prompt_variables),
        )
        
        return response
