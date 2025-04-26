"""Agent module initialization.

This module provides access to all agents in the system.
"""
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from models import deepseek_v3, embedding_model, o3_mini, gpt_4o, gpt4_mini
from agents.toc_agent import TOCAgent
from agents.code_agent import CodeAgent
from agents.debug_agent import DebugAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.document_retriever import DocumentRetriever
from agents.error_analyzer_agent import ErrorAnalyzerAgent
from agents.review_agent import ReviewAgent

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)

manim_ce_index = pc.Index("manim-ce")
manim_voiceover_index = pc.Index("manim-voiceover")

manim_ce_vectorstore = PineconeVectorStore(index=manim_ce_index, embedding=embedding_model)
manim_voiceover_vectorstore = PineconeVectorStore(index=manim_voiceover_index, embedding=embedding_model)

toc_agent = TOCAgent(
    llm=deepseek_v3,
    max_subtopics=8,  # Reasonable limit for most topics
    target_video_duration=2.5  # Target of 2-5 minutes per subtopic
)

code_agent = CodeAgent(
    llm=deepseek_v3
)

debug_agent = DebugAgent(
    llm=deepseek_v3
)

question_generator = QuestionGeneratorAgent(
    llm=deepseek_v3
)

error_analyzer = ErrorAnalyzerAgent(
    llm=deepseek_v3
)

review_agent = ReviewAgent(
    llm=deepseek_v3
)

document_retriever = DocumentRetriever(manim_ce_vectorstore, manim_voiceover_vectorstore)

# Example of generating a table of contents:
# toc = toc_agent.generate_toc(
#     topic="Linear Algebra",
#     audience="high school students"
# )

# Example of generating questions and retrieving documentation:
# questions = question_generator.generate_questions(
#     topic="Linear Algebra",
#     key_points="Vectors, Matrices, Linear Transformations",
#     duration=10
# )
# docs = document_retriever.retrieve_docs(questions)

# Example of generating an animation with documentation:
# animation = code_agent.generate_animation(
#     topic="Linear Algebra",
#     key_points="Vectors, Matrices, Linear Transformations",
#     duration=10,
#     relevant_docs=docs
# )

# Example of fixing an animation with errors:
# error_analysis = error_analyzer.analyze_errors(
#     original_code=animation_code,
#     error_log=error_message,
#     original_script=script
# )
# error_questions = error_analysis["questions"]
# error_docs = document_retriever.retrieve_docs(error_questions)
# fixed_animation = debug_agent.fix_animation(
#     original_code=animation_code,
#     error_log=error_message,
#     original_script=script,
#     error_analysis=error_analysis["error_summary"],
#     relevant_docs=error_docs
# )

# Example of reviewing an animation:
# review_result = review_agent.review_animation(
#     original_code=animation_code,
#     topic="Linear Algebra",
#     topic_description="Vectors, Matrices, Linear Transformations",
#     duration=10
# )