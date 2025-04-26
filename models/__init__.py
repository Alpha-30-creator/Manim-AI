"""Initialize core models for the Manim-AI project."""
from dotenv import load_dotenv
import os

# Import model classes from their respective modules
from models.azure import GPT4o, GPT4Mini, O3Mini, Embedding
from models.openrouter import ChatOpenRouter
from models.deepseek import DeepSeek_V3

# Load environment variables
load_dotenv()

# Initialize Azure models using the factory classes
gpt_4o = GPT4o.get_instance()
gpt4_mini = GPT4Mini.get_instance()
o3_mini = O3Mini.get_instance()
embedding_model = Embedding.get_instance()

# Initialize DeepSeek V3
deepseek_v3 = DeepSeek_V3.get_instance()
