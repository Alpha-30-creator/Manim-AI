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
- ✅ **Azure OpenAI Integration**: Configured to work with different model deployments
- ✅ **Token Usage Monitoring**: Tracks API usage for better resource management
- ✅ **Time-Optimized Content Planning**: Designs subtopics to fit specific time constraints

## Project Structure

```
Manim-AI/
├── agents/                  # AI agents for different generation tasks
│   ├── __init__.py          # Agent module initialization
│   └── toc_agent.py         # TOC generation agent (implemented)
├── models/                  # LLM model connections and configurations
│   ├── __init__.py          # Model instances initialization
│   └── azure.py             # Azure OpenAI connection management
├── tests/                   # Test modules and scripts
│   ├── __init__.py          # Test package initialization
│   └── toc_agent_test.py    # Tests for TOC generation agent
├── docs/                    # Manim documentation and reference materials
├── outputs/                 # Generated TOC outputs and other artifacts
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

4. Configure Azure OpenAI credentials:
   - Create a `.env` file or edit `models/azure.py` with your Azure credentials:
     - API key
     - Endpoint URL
     - Model deployments

## Usage

### Testing the TOC Generation

Run the TOC generation test to verify the system's ability to structure mathematical topics:

```
python -m tests.toc_agent_test
```

This will generate structured tables of contents for several mathematical topics (Linear Algebra, Calculus, Probability Theory, Number Theory) and save them as JSON files in the `outputs/` directory.

### Sample Output

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

## Roadmap

### Next Development Phases

1. **Script Generation Agent** (Next Priority)
   - Create detailed educational scripts for each subtopic
   - Ensure script timing matches planned durations
   - Include speaker notes and key visualizations

2. **Manim Code Generation**
   - Develop system to translate script requirements into Manim animation code
   - Ensure proper visualization of mathematical concepts
   - Create modular, reusable animation components

3. **Rendering Pipeline**
   - Build end-to-end pipeline from topic to rendered video
   - Add audio narration capabilities (text-to-speech)
   - Implement quality assurance checks

4. **User Interface**
   - Create web interface for topic selection and customization
   - Provide real-time preview of generated content
   - Allow manual editing of generated scripts and animations

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