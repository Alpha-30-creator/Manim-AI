# Manim-AI

An AI-powered system for generating educational animations using Manim and synchronized voiceovers.

## Overview

Manim-AI is a specialized system that combines the power of large language models with Manim (Mathematical Animation Engine) to automatically generate educational animations with synchronized voiceovers. The system uses a modular, agent-based architecture to handle the complex process of animation generation, from topic planning to code generation and debugging.

## Features

- **Topic-Based Animation Generation**: Create animations from high-level topic descriptions
- **Synchronized Voiceovers**: Automatically generate and synchronize voiceovers with animations using Azure TTS
- **Modular Agent Architecture**: Specialized agents for each part of the generation process
- **Documentation-Aware**: Leverages Manim and Manim-Voiceover documentation for accurate code generation
- **Error Handling**: Automatic debugging and error correction
- **Educational Structure**: Built-in educational narrative construction

## Requirements

- Python 3.9+
- Manim CE 0.19.0+
- Manim-Voiceover 0.3.7+
- Azure Speech Service account (for voiceovers)
- Pinecone account (for vector search)
- OpenAI or Azure OpenAI API access

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Manim-AI.git
   cd Manim-AI
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Manim dependencies according to [Manim installation guide](https://docs.manim.community/en/stable/installation.html)

5. Create a `.env` file with your API keys:
   ```
   # Azure OpenAI
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_KEY=your_azure_openai_key
   
   # Azure Speech Service
   AZURE_SUBSCRIPTION_KEY=your_azure_speech_key
   AZURE_SERVICE_REGION=your_azure_region
   
   # Pinecone
   PINECONE_API_KEY=your_pinecone_api_key
   
   # OpenRouter 
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

## System Architecture

Manim-AI uses a multi-agent architecture to break down the complex task of animation generation:

1. **TOC Agent** (`TOCAgent`): Generates a structured table of contents for a given educational topic
2. **Question Generator** (`QuestionGeneratorAgent`): Generates questions about Manim functionality needed for implementation
3. **Document Retriever** (`DocumentRetriever`): Retrieves relevant documentation for questions from vector stores
4. **Code Agent** (`CodeAgent`): Generates Manim animation code with synchronized voiceover
5. **Error Analyzer** (`ErrorAnalyzerAgent`): Analyzes error logs and generates relevant questions for debugging
6. **Debug Agent** (`DebugAgent`): Fixes errors in generated animations
7. **Review Agent** (`ReviewAgent`): Reviews and improves generated animations

## Usage Examples

### Basic Animation Generation

```python
from agents import (
    question_generator, document_retriever, code_agent
)

# 1. Generate questions about Manim functionality
questions = question_generator.generate_questions(
    topic="Quantum Computing Basics",
    key_points="Qubits, Superposition, Quantum Gates, Measurement",
    duration=10
)

# 2. Retrieve relevant documentation
docs = document_retriever.retrieve_docs(questions)

# 3. Generate the animation
animation = code_agent.generate_animation(
    topic="Quantum Computing Basics",
    topic_description="Qubits, Superposition, Quantum Gates, Measurement",
    duration=10,
    relevant_docs=docs
)

# Save the result
with open("output/quantum_computing.py", "w") as f:
    # Include imports
    for import_stmt in animation["imports"]:
        f.write(f"{import_stmt}\n")
    
    # Add a blank line between imports and scene code
    f.write("\n")
    
    # Write the scene code
    f.write(animation["scene_code"])

# Print the command to run the animation
print(animation["run_command"])
```

### Complete End-to-End Process (including error handling)

See `tests/main_test.py` for a complete example of the end-to-end process, including:
- Animation generation
- Error analysis
- Debugging
- Re-running the fixed animation

## Vector Store Setup

The system uses Pinecone vector stores for Manim and Manim-Voiceover documentation. The `vectorizer` directory contains tools for processing and uploading documentation.

