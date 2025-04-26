"""Module to load Azure OpenAI models."""
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

# Load environment variables from .env file (as backup)
load_dotenv()

# Hard-coded Azure OpenAI Configuration - no comments, no whitespace issues
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

# Hard-coded deployment names and API versions
GPT4O_DEPLOYMENT = os.getenv("AZURE_GPT4_DEPLOYMENT")
GPT4_MINI_DEPLOYMENT = os.getenv("AZURE_GPT4_MINI_DEPLOYMENT")
GPT4_API_VERSION = os.getenv("AZURE_GPT4_API_VERSION")
O3_MINI_DEPLOYMENT = os.getenv("AZURE_O3_MINI_DEPLOYMENT")
O3_API_VERSION = os.getenv("AZURE_O3_API_VERSION")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")
EMBEDDING_API_VERSION = os.getenv("AZURE_EMBEDDING_API_VERSION")

class GPT4Mini:
    """Class to load GPT-4 Mini model for TOC and script generation."""
    
    @staticmethod
    def get_instance():
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=GPT4_MINI_DEPLOYMENT,
            api_version=GPT4_API_VERSION,
            temperature=0.3
        )
    
class GPT4o:
    """Class to load GPT-4o model for TOC and script generation."""
    
    @staticmethod
    def get_instance():
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=GPT4O_DEPLOYMENT,
            api_version=GPT4_API_VERSION,
            temperature=0.1
        )

class O3Mini:
    """Class to load O3 Mini model for Manim code generation and debugging."""
    
    @staticmethod
    def get_instance():
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=O3_MINI_DEPLOYMENT,
            api_version=O3_API_VERSION
        )

class Embedding:
    """Class to load Azure Embedding model."""
    
    @staticmethod
    def get_instance():
        return AzureOpenAIEmbeddings(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=EMBEDDING_API_VERSION,
            azure_deployment=EMBEDDING_DEPLOYMENT,
            dimensions=1024  # Match Pinecone index dimension
        )
