from app.agents.builder_evaluate_agent import build_evaluator_agent

from app.prompts.evaluation_prompt import (
    EVALUATION_USER_PROMPT
)


evaluator_agent = build_evaluator_agent()


async def evaluate_research(
    query: str,
    research_response: str
):

    user_prompt = EVALUATION_USER_PROMPT.format(
        query=query,
        research_response=research_response
    )

    response = await evaluator_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }
    )

    return response["messages"][-1].content