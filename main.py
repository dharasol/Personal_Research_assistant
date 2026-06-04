from dotenv import load_dotenv
load_dotenv()  # ← must be FIRST, before any other imports

import litellm
litellm.drop_params = True  # ← second, before CrewAI imports

from crew import research_crew  # ← now imports happen after env is loaded

def run(topic: str):
    result = research_crew.kickoff(inputs={"topic": topic})
    print("-" * 50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    topic = "AI Agents"
    run(topic)