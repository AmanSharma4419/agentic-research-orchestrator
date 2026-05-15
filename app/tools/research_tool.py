from langchain.tools import tool
from app.services.tavily_service import search_web

@tool
async def tavily_research_tool(query:str):
    """
    Search in web for recent information.
    Useful for research and latest updates.
    """
    
    results = await search_web(query)
    
    return results.get("results",[])