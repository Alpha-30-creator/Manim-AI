"""Agent module initialization.

This module provides access to all agents in the system.
"""

from models import gpt4_mini
from agents.toc_agent import TOCAgent
from agents.script_agent import ScriptAgent


toc_agent = TOCAgent(
    llm=gpt4_mini,
    max_subtopics=8,  # Reasonable limit for most topics
    target_video_duration=2.5  # Target of 2-5 minutes per subtopic
)

script_agent = ScriptAgent(
    llm=gpt4_mini
)

# Example usage:
# toc = toc_agent.generate_toc(
#     topic="Linear Algebra",
#     audience="high school students"
# )

# Example of generating a script:
# script = script_agent.generate_script(
#     subtopic_title="Introduction to Vectors",
#     duration=2.5,
#     audience="high school students",
#     difficulty="beginner",
#     prerequisites=["Basic Algebra"],
#     key_points=["Vector definition", "Vector operations", "Geometric interpretation"]
# )
