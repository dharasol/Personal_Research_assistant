from crewai import Crew, LLM
import litellm
import os
from dotenv import load_dotenv
load_dotenv()

litellm.drop_params = True  # ← must be before any imports that trigger LLM calls

from agents.research_specialist import research_specialist_agent
from agents.data_analyst import data_analyst_agent
from agents.content_writer import content_writer_agent
from tasks.research_task import research_task
from tasks.analysis_task import analysis_task
from tasks.writing_task import writing_task

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    drop_params=True  # ← add here too
)

research_crew = Crew(
    agents=[
        research_specialist_agent,
        data_analyst_agent,
        content_writer_agent,
    ],
    tasks=[
        research_task,
        analysis_task,
        writing_task,
    ],
    verbose=True,
    prompt_cache=False,
    max_rpm=5,
    memory=False,
)