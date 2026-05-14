from app.services.tavily_service import search_web
from app.services.llm_service import llm
from app.prompts.research_prompt import RESEARCH_SUMMARY_PROMPT


async def run_research_chain(query: str):

    search_results = await search_web(query)

    results = search_results.get("results", [])

    formatted_results = ""

    for index, result in enumerate(results, start=1):

        formatted_results += f"""
        
SOURCE {index}

Title:
{result.get("title")}

URL:
{result.get("url")}

Content:
{result.get("content")}

"""

    prompt = RESEARCH_SUMMARY_PROMPT.format(
        query=query,
        results=formatted_results
    )

    response = await llm.ainvoke(prompt)

    return {
        "query": query,
        "search_results": results,
        "summary": response.content
    }