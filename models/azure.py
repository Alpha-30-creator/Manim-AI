"""Module to load Azure OpenAI models."""
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

# Load environment variables from .env file (as backup)
load_dotenv()

# Hard-coded Azure OpenAI Configuration - no comments, no whitespace issues
AZURE_OPENAI_API_KEY = "8df98ecfe8db47bd8ff11e0b7033a273"  # Hard-coded from your .env
AZURE_OPENAI_ENDPOINT = "https://engineering-and-archaeology.openai.azure.com/"

# Hard-coded deployment names and API versions
GPT4_MINI_DEPLOYMENT = "gpt-4o-mini"
GPT4_API_VERSION = "2024-05-01-preview"
O3_MINI_DEPLOYMENT = "o3-mini"
O3_API_VERSION = "2024-12-01-preview"
EMBEDDING_DEPLOYMENT = "Embedding-Large"
EMBEDDING_API_VERSION = "2023-05-15"

class GPT4Mini:
    """Class to load GPT-4 Mini model for TOC and script generation."""
    
    @staticmethod
    def get_instance():
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=GPT4_MINI_DEPLOYMENT,
            api_version=GPT4_API_VERSION,
            temperature=0
        )

class O3Mini:
    """Class to load O3 Mini model for Manim code generation and debugging."""
    
    @staticmethod
    def get_instance():
        return AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            azure_deployment=O3_MINI_DEPLOYMENT,
            api_version=O3_API_VERSION,
            temperature=0
        )

class Embedding:
    """Class to load Azure Embedding model."""
    
    @staticmethod
    def get_instance():
        return AzureOpenAIEmbeddings(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=EMBEDDING_API_VERSION,
            azure_deployment=EMBEDDING_DEPLOYMENT
        )
