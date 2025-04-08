import os
import time
from dotenv import load_dotenv
from crewai import Crew, Task, Process
from langchain_openai import ChatOpenAI
from agents import StoryAgents

# Load environment variables
load_dotenv()

def get_user_feedback(message):
    """Get feedback from the user."""
    print("\n" + "="*50)
    print(message)
    return input("Your feedback: ")

def main():
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set your OPENAI_API_KEY environment variable.")
        print("You can create a .env file with the content: OPENAI_API_KEY=your-api-key")
        return
    
    # Get story parameters
    print("Welcome to the Interactive Storybook Creator!")
    story_type = input("Enter a general theme for your story (e.g., adventure, mystery, fantasy): ") or "adventure"
    story_length = input("Enter desired story length (short, medium, long): ") or "medium"
    
    # Map story length to approximate word count
    length_map = {
        "short": "around 500 words",
        "medium": "around 1000 words",
        "long": "around 2000 words"
    }
    word_count = length_map.get(story_length.lower(), "around 1000 words")
    
    # Initialize language model
    llm = ChatOpenAI(model="gpt-4o")
    
    # Create agents
    story_agents = StoryAgents(llm=llm)
    planner = story_agents.create_planner_agent()
    writer = story_agents.create_writer_agent()
    editor = story_agents.create_editor_agent()
    analyzer = story_agents.create_analyzer_agent()
    
    # Create tasks
    planning_task = Task(
        description=f"""
        Create a story outline for a {story_type} story that will be {word_count}.
        
        Include:
        1. A brief summary of the plot
        2. Main characters with short descriptions
        3. Setting description
        4. 3-5 key plot points or scenes
        
        Be creative and engaging!
        """,
        agent=planner,
        expected_output="A detailed story outline with plot, characters, and setting."
    )
    
    # Initialize with empty outline that will be updated after planning task
    outline = ""
    
    writing_task = Task(
        description=f"""
        Write a {story_type} story based on the following outline:
        
        {{outline}}
        
        The story should be {word_count}.
        
        Make sure to:
        1. Follow the outline's plot points
        2. Develop the characters as described
        3. Use the setting effectively
        4. Create engaging dialogue and descriptions
        
        Write the complete story with a beginning, middle, and end.
        """,
        agent=writer,
        expected_output="A complete story based on the provided outline."
    )
    
    # Initialize with empty story that will be updated after writing task
    story = ""
    
    editing_task = Task(
        description=f"""
        Edit and refine the following story:
        
        {{story}}
        
        Focus on:
        1. Improving clarity and flow
        2. Enhancing descriptions and dialogue
        3. Ensuring consistency in plot and characters
        4. Fixing any grammatical or spelling errors
        5. Making sure the story is engaging and approximately {word_count}
        
        Provide the complete edited story.
        """,
        agent=editor,
        expected_output="A polished, refined version of the story."
    )

    analysing_task = Task(
        description=f"""
            Analyse the characters in the following story:

            {{story}}

            Focus on:
            1. Judge if each character is a good person or bad person
            2. Guess what thet are possibly thinking when doing things or communicating
            3. Transfer what they think into sentences they may say
            4. Fixing any grammatical or spelling errors
            5. Making sure the story is engaging and approximately {word_count}

            Provide the complete edited story.
            """,
        agent=editor,
        expected_output="A polished, refined version of the story."
    )
    
    # Create the crew
    crew = Crew(
        agents=[planner, writer, editor, analyzer],
        tasks=[planning_task],
        process=Process.sequential
    )
    
    # Step 1: Planning
    print("\nStarting the story planning process...")
    result = crew.kickoff()
    outline = result
    
    print("\nStory Outline:")
    print(outline)
    
    # Get user feedback on the outline
    feedback = get_user_feedback("What feedback do you have on this outline?")
    
    # Update the writing task with the outline and feedback
    writing_task.description = writing_task.description.format(
        outline=f"{outline}\n\nFeedback on the outline: {feedback}"
    )
    
    # Step 2: Writing
    crew = Crew(
        agents=[writer, editor, analyzer],
        tasks=[writing_task],
        process=Process.sequential
    )
    
    print("\nStarting the story writing process...")
    result = crew.kickoff()
    story = result
    
    print("\nDraft Story:")
    print(story)
    
    # Get user feedback on the draft
    feedback = get_user_feedback("What feedback do you have on this draft?")
    
    # Update the editing task with the story and feedback
    editing_task.description = editing_task.description.format(
        story=f"{story}\n\nFeedback on the draft: {feedback}"
    )

    # Step 3: Analysing
    crew = Crew(
        agents=[writer, editor, analyzer],
        tasks=[analysing_task],
        process=Process.sequential
    )

    print("\nStarting the story writing process...")
    result = crew.kickoff()
    story = result

    print("\nDraft Story:")
    print(story)

    # Get user feedback on the draft
    feedback = get_user_feedback("What feedback do you have on this draft?")

    # Update the editing task with the story and feedback
    editing_task.description = editing_task.description.format(
        story=f"{story}\n\nFeedback on the draft: {feedback}"
    )
    
    # Step 4: Editing
    crew = Crew(
        agents=[editor],
        tasks=[editing_task],
        process=Process.sequential
    )
    
    print("\nStarting the story editing process...")
    result = crew.kickoff()
    final_story = result
    
    print("\nFinal Story:")
    print(final_story)
    

    
    # Save the story to a file
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"output/story_{timestamp}.docx"
    
    os.makedirs("output", exist_ok=True)
    
    with open(filename, "w") as f:
        f.write(f"# {story_type.title()} Story\n\n")
        f.write(str(final_story))

    print(f"\nStory saved to {filename}")

if __name__ == "__main__":
    main()
