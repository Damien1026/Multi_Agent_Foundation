from crewai import Agent
from langchain_openai import ChatOpenAI

class StoryAgents:
    def __init__(self, llm=None):
        """Initialize the story agents with a language model.
        
        Args:
            llm: Language model to use for the agents. If None, a default model will be used.
        """
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_planner_agent(self):
        """Create an agent responsible for planning the story outline."""
        return Agent(
            role="Story Planner",
            goal="Create a compelling story outline with plot points and characters",
            backstory="""You are an experienced story planner who excels at creating 
            engaging narratives. Your job is to create a story outline that includes 
            the main plot points, characters, and setting.""",
            verbose=True,
            llm=self.llm,
            tools=[]
        )
    
    def create_writer_agent(self):
        """Create an agent responsible for writing the story content."""
        return Agent(
            role="Story Writer",
            goal="Write engaging and coherent story content based on the provided outline",
            backstory="""You are a talented writer who can transform story outlines 
            into engaging narratives. Your job is to write the actual story content 
            based on the outline provided by the Story Planner.""",
            verbose=True,
            llm=self.llm,
            tools=[]
        )
    
    def create_editor_agent(self):
        """Create an agent responsible for editing and refining the story."""
        return Agent(
            role="Story Editor",
            goal="Refine and improve the story for clarity, coherence, and engagement",
            backstory="""You are a meticulous editor with an eye for detail and narrative flow. 
            Your job is to review and refine the story content to ensure it is coherent, 
            engaging, and free of errors.""",
            verbose=True,
            llm=self.llm,
            tools=[]
        )

    def create_analyzer_agent(self):
        """Create an agent responsible for analysing what our characteristics are thinking."""
        return Agent(
            role="Character Analyzer",
            goal="Analyse what our characteristics are thinking.",
            backstory="""You are a Character Analyzer with the ability to analyze what kind of role our characteristics are (good or bad), and analyze what they are thinking. 
            Your job is to guess what our characteristics are possibly thinking and put what they think into the sentences they may use for communicate.""",
            verbose=True,
            llm=self.llm,
            tools=[]
        )

