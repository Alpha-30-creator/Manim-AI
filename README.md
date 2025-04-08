# Manim-AI

An intelligent system combining Manim (Mathematical Animation Engine) with Azure OpenAI to automatically generate engaging educational mathematics videos.

## Project Vision

Manim-AI aims to revolutionize the creation of educational mathematics content by automating the video creation process from topic selection to final rendering. The system uses large language models to:

1. Structure mathematical topics into logical learning sequences
2. Generate time-optimized educational content for each subtopic
3. Produce Manim animation code that effectively visualizes concepts
4. Render complete educational videos with minimal human intervention

This approach enables educators to rapidly create professional-quality mathematical animations tailored to specific audiences and learning objectives.

## Current Project Status

The project is in active development, with the following components implemented:

- ✅ **TOC Generation Agent**: Creates structured tables of contents with proper learning progressions
- ✅ **Script Generation Agent**: Generates detailed educational scripts for each subtopic
- ✅ **Azure OpenAI Integration**: Configured to work with different model deployments
- ✅ **Token Usage Monitoring**: Tracks API usage for better resource management
- ✅ **Time-Optimized Content Planning**: Designs subtopics to fit specific time constraints
- ✅ **Manim Documentation Vectorization**: Converts Manim documentation into embeddings for RAG applications

## Project Structure

```
Manim-AI/
├── agents/                  # AI agents for different generation tasks
│   ├── __init__.py          # Agent module initialization
│   ├── toc_agent.py         # TOC generation agent (implemented)
│   └── script_agent.py      # Script generation agent (implemented)
├── models/                  # LLM model connections and configurations
│   ├── __init__.py          # Model instances initialization
│   └── azure.py             # Azure OpenAI connection management
├── tests/                   # Test modules and scripts
│   ├── __init__.py          # Test package initialization
│   ├── toc_agent_test.py    # Tests for TOC generation agent
│   └── script_agent_test.py # Tests for script generation agent
├── vectorizer/              # Documentation vectorization tools
│   ├── utils.py             # Utility functions for vectorization
│   ├── vectorizer.py        # Main vectorization script
│   ├── manim-ce-cleaned/    # Processed Manim CE documentation
│   └── manim-voiceover-cleaned/ # Processed Manim Voiceover documentation
├── docs/                    # Manim documentation and reference materials
├── outputs/                 # Generated outputs and artifacts
│   ├── toc_outputs/         # Generated TOC JSON files
│   └── script_outputs/      # Generated script JSON files
├── main.py                  # Main entry point
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables (not in repository)
```

## Key Features

### TOC Generation Agent

- Creates structured tables of contents for mathematical topics
- Ensures proper learning sequence with prerequisites
- Provides realistic time estimates for each subtopic (1-5 minutes)
- Tailors content to specific audience levels (high school, undergraduate, etc.)
- Varies difficulty appropriately through the topic progression

### Script Generation Agent

- Generates detailed educational scripts for each mathematical subtopic
- Creates structured content blocks optimized for teaching efficiency
- Designs appropriate visual elements to illustrate concepts
- Includes LaTeX equations for mathematical notation
- Adapts content to match target audience and difficulty level
- Manages timing to fit within specified duration constraints

### Manim Documentation Vectorization

- Processes cleaned Manim documentation from CE and Voiceover libraries
- Intelligently chunks documentation by headings while preserving code blocks
- Extracts rich metadata including document type, title, parent headings, and code elements
- Generates high-quality embeddings using Azure OpenAI
- Uploads documents and metadata to Pinecone vector database for RAG applications
- Provides robust error handling and resumable processing

### Time-Optimized Content Design

- Intelligently structures content to fit specific time constraints
- Varies durations based on subtopic complexity:
  - Simple topics: 1-2 minutes
  - Moderate complexity: 2-3 minutes
  - Complex topics: 3-5 minutes
- Balances key points and depth based on available time

## Setup and Installation

### Prerequisites

- Python 3.8+
- Azure OpenAI API access with appropriate model deployments
- Pinecone API key (for vectorization functionality)
- LangChain and related libraries

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Manim-AI.git
   cd Manim-AI
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure API keys in the `.env` file:
   ```
   # Azure OpenAI
   AZURE_OPENAI_API_KEY=your_azure_openai_key
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint
   
   # Pinecone
   PINECONE_API_KEY=your_pinecone_api_key
   ```

## Usage

### Testing the TOC Generation

Run the TOC generation test to verify the system's ability to structure mathematical topics:

```
python -m tests.toc_agent_test
```

This will generate structured tables of contents for several mathematical topics (Linear Algebra, Calculus, Probability Theory, Number Theory) and save them as JSON files in the `outputs/toc_outputs/` directory.

### Testing the Script Generation

Run the script generation test to generate educational scripts for subtopics:

```
python -m tests.script_agent_test
```

This will generate detailed educational scripts for a sample mathematical subtopic and save it as a JSON file in the `outputs/script_outputs/` directory.

### Running the Documentation Vectorization

Process the Manim documentation and upload it to Pinecone:

```
python -m vectorizer.vectorizer
```

Additional options:
```
# Process only Manim CE documentation
python -m vectorizer.vectorizer --only manim-ce

# Process only Manim Voiceover documentation
python -m vectorizer.vectorizer --only manim-voiceover

# Skip already processed files (resume from last state)
python -m vectorizer.vectorizer --skip-existing
```

### Sample Output

#### TOC Generation

The TOC agent generates structured JSON content like this:

```json
{
  "main_topic": "Linear Algebra Fundamentals",
  "description": "An introduction to essential concepts of linear algebra...",
  "difficulty": "intermediate",
  "audience": "undergraduate students",
  "subtopics": [
    {
      "title": "Introduction to Vectors",
      "order_index": 1,
      "estimated_duration": 1.5,
      "difficulty": "beginner",
      "prerequisites": [],
      "key_points": [
        "Definition of vectors",
        "Representation in 2D and 3D",
        "Basic operations"
      ]
    },
    // Additional subtopics...
  ]
}
```

#### Script Generation

The Script agent generates detailed educational content like this:

```json
{
  "subtopic_title": "Introduction to Vectors",
  "total_duration_minutes": 2.5,
  "target_audience": "high school students",
  "difficulty": "beginner",
  "content_blocks": [
    {
      "type": "conceptual explanation",
      "title": "What is a Vector?",
      "content": "A vector is a mathematical object that has both magnitude and direction...",
      "duration": 0.5
    },
    {
      "type": "visual/geometric interpretation",
      "title": "2D and 3D Representation",
      "content": "Vectors can be represented graphically as arrows...",
      "duration": 0.5
    },
    // Additional content blocks...
  ],
  "visual_elements": [
    {
      "description": "Graphical representation of a vector in 2D and 3D",
      "timing": "0:30",
      "details": "Show an arrow from the origin to a point (x,y) in a 2D coordinate system..."
    },
    // Additional visual elements...
  ],
  "equations": [
    "\\\\mathbf{v} = \\\\begin{pmatrix} x \\\\ y \\\\end{pmatrix}",
    // Additional equations...
  ],
  "key_concepts": [
    "Definition of vectors",
    "Representation in 2D and 3D",
    // Additional key concepts...
  ]
}
```

## Roadmap

### Next Development Phases

1. **RAG-Enhanced Code Generation** (Next Priority)
   - Leverage vectorized Manim documentation for context-aware code generation
   - Implement retrieval-augmented generation for more accurate animation code
   - Ensure proper visualization of mathematical concepts with Manim best practices

2. **Manim Code Generation**
   - Develop system to translate script requirements into Manim animation code
   - Create modular, reusable animation components
   - Add code validation and testing

3. **Rendering Pipeline**
   - Build end-to-end pipeline from topic to rendered video
   - Add audio narration capabilities (text-to-speech)
   - Implement quality assurance checks

### Long-Term Vision

- Support for multiple languages and educational levels
- Interactive elements in generated videos
- Integration with educational platforms
- Custom branding and styling options
- Expand beyond mathematics to other STEM subjects

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Your license information here] 