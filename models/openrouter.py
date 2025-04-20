"""OpenRouter integration for accessing various LLMs through a unified API."""
import os
from typing import Optional

from dotenv import load_dotenv
from langchain_core.utils.utils import secret_from_env
from langchain_openai import ChatOpenAI
from pydantic import Field, SecretStr

# Load environment variables
load_dotenv()

class ChatOpenRouter(ChatOpenAI):
    """ChatOpenAI wrapper for OpenRouter API.
    
    OpenRouter provides a unified API for accessing various LLMs including
    Claude, Mistral, DeepSeek, and others using OpenAI's API format.
    """
    
    openai_api_key: Optional[SecretStr] = Field(
        alias="api_key",
        default_factory=secret_from_env("OPENROUTER_API_KEY", default=None),
    )
    
    @property
    def lc_secrets(self) -> dict[str, str]:
        """Define secrets for serialization."""
        return {"openai_api_key": "OPENROUTER_API_KEY"}
    
    def __init__(self,
                 openai_api_key: Optional[str] = None,
                 **kwargs):
        """Initialize the OpenRouter client.
        
        Args:
            openai_api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY env var)
            **kwargs: Additional arguments to pass to ChatOpenAI
        """
        openai_api_key = (
            openai_api_key or os.environ.get("OPENROUTER_API_KEY")
        )
        super().__init__(
            base_url="https://openrouter.ai/api/v1",
            openai_api_key=openai_api_key,
            **kwargs
        ) 