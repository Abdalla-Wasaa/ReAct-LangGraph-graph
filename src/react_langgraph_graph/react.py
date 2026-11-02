from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openrouter import ChatOpenRouter
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to be tripled
    returns: the triple of a number.
    """
    return float(num) * 3

tools = [triple, TavilySearch(max_results=1)]

llm=ChatOpenRouter(model="gpt-4o-mini", temperature=0).bind_tools(tools)