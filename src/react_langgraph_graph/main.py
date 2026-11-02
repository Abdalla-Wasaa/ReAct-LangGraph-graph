import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Starting the ReAct-LangGraph-graph application...")
    print(os.environ.get("OPENROUTER_API_KEY"))