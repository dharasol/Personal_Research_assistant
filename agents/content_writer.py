import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool
from dotenv import load_dotenv
load_dotenv()

# LLM configurations - Agent specific config
model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE","0.5"))

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)
