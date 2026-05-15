from langchain.agents import create_agent
from app.services.llm_service import llm
from app.tools.research_tool import tavily_research_tool

def build_research_agent():

    tools = [tavily_research_tool]

    agent = create_agent(
        model=llm,
        tools=tools
    )

    return agent