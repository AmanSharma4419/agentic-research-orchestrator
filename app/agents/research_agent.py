from app.agents.builder_research_agent import build_research_agent
from app.agents.evaluator_agent import evaluate_research

research_agent = build_research_agent()


async def run_research_agent(query: str):

    response = await research_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    research_response = response["messages"][-1].content


    evaluation  = await evaluate_research(
        query=query,
        research_response=research_response
    )
    
    
    return {
        "query": query,
        "research_answer": research_response,
        "evaluation": evaluation
    }

  
    
    
    