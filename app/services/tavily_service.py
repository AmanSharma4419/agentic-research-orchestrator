import os
from tavily import TavilyClient

from app.core.config import settings

tavily_client = TavilyClient(
    api_key= settings.TAVILY_API_KEY
)


async def search_web(query: str):

    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response