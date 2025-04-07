"""Agent module initialization.

This module provides access to all agents in the system.
"""

from models.azure import GPT4Mini
from agents.toc_agent import TOCAgent


toc_agent = TOCAgent(
    llm=GPT4Mini.get_instance(),
    max_subtopics=8,  # Reasonable limit for most topics
    target_video_duration=2.5  # Target of 2-3 minutes per subtopic
)

# Example usage:
# toc = toc_agent.generate_toc(
#     topic="Linear Algebra",
#     audience="high school students"
# )
