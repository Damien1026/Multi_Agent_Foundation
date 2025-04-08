# Interactive Multi-Agent Storybook Creator

This is a simple tutorial example of using Crew AI to create a multi-agent system that collaboratively writes a storybook. The system uses three specialized agents that work together in an interactive process:

1. **Story Planner**: Creates the story outline with plot, characters, and setting
2. **Story Writer**: Writes the actual story based on the outline
3. **Story Editor**: Refines and improves the story

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the main script to start the interactive storybook creation process:

```bash
python main.py
```

The script will:

1. Ask for your story preferences (theme and length)
2. Generate a story outline using the Planner Agent
3. Ask for your feedback on the outline
4. Write a draft story using the Writer Agent
5. Ask for your feedback on the draft
6. Refine the story using the Editor Agent
7. Ask for your final feedback
8. Save the completed story to the output directory

## Example Workflow

```
Welcome to the Interactive Storybook Creator!
Enter a general theme for your story (e.g., adventure, mystery, fantasy): fantasy
Enter desired story length (short, medium, long): short

Starting the story planning process...
[Agent execution details...]

Story Outline:
[Generated outline appears here]

==================================================
What feedback do you have on this outline?
[User provides feedback]

Starting the story writing process...
[Agent execution details...]

Draft Story:
[Generated story appears here]

==================================================
What feedback do you have on this draft?
[User provides feedback]

Starting the story editing process...
[Agent execution details...]

Final Story:
[Final edited story appears here]

==================================================
What do you think of the final story?
[User provides final feedback]

Story saved to output/story_20250315-102845.txt
```

## How It Works

This example demonstrates several key concepts in multi-agent systems:

1. **Specialized Agents**: Each agent has a specific role and expertise
2. **Sequential Workflow**: Agents work in a logical sequence to build upon each other's work
3. **Interactive Feedback**: The system incorporates user feedback at each stage
4. **Task-based Approach**: Each agent is assigned specific tasks with clear expectations

The implementation uses Crew AI's framework to orchestrate the agents and manage the workflow, making it easy to create collaborative AI systems.

## Customization

You can extend this example by:

- Adding more specialized agents (e.g., a Character Developer or Illustrator)
- Implementing more sophisticated feedback mechanisms
- Adding tools for the agents to use (e.g., web search, reference checking)
- Creating a more complex workflow with parallel tasks

## Requirements

- Python 3.12
- OpenAI API key
- Crew AI library
- LangChain
