import os
from langchain_deepseek import ChatDeepSeek

class DeepSeek_V3:
    """
    Class to load DeepSeek V3 model
    """
    @staticmethod
    def get_instance():
        return ChatDeepSeek(
            model="deepseek-chat",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=0.1
        )
