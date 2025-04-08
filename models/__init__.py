"""Initialize core Azure OpenAI models."""
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import os

# Hard-coded Azure OpenAI Configuration
AZURE_OPENAI_API_KEY = "8df98ecfe8db47bd8ff11e0b7033a273"
AZURE_OPENAI_ENDPOINT = "https://engineering-and-archaeology.openai.azure.com/"

# Hard-coded deployment names and API versions
GPT4_MINI_DEPLOYMENT = "gpt-4o-mini"
GPT4_API_VERSION = "2024-05-01-preview"
O3_MINI_DEPLOYMENT = "o3-mini"
O3_API_VERSION = "2024-12-01-preview"
EMBEDDING_DEPLOYMENT = "APSAP-test-text-embedding-3-large"
EMBEDDING_API_VERSION = "2024-12-01-preview"

# Initialize GPT-4 Mini model (for TOC and script generation)
# Lower temperature (0.3) for more focused, consistent outputs
gpt4_mini = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    azure_deployment=GPT4_MINI_DEPLOYMENT,
    api_version=GPT4_API_VERSION,
    temperature=0.3  # Balanced between creativity and consistency
)

# Initialize O3 Mini model (for Manim code generation, review, and debugging)
# Very low temperature (0.1) for precise, deterministic code generation
o3_mini = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    azure_deployment=O3_MINI_DEPLOYMENT,
    api_version=O3_API_VERSION,
    temperature=0.1  # More deterministic for code generation
)

# Initialize embedding model
embedding_model = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=EMBEDDING_API_VERSION,
    azure_deployment=EMBEDDING_DEPLOYMENT
)