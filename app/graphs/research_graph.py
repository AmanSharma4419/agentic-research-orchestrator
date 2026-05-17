import json
from typing import TypedDict
from app.agents.builder_research_agent import build_research_agent
from app.agents.builder_evaluate_agent import build_evaluator_agent
from app.prompts.evaluation_prompt import EVALUATION_USER_PROMPT
from app.db.checkpointer import checkpointer

from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt

research_agent = build_research_agent()
evaluate_agent = build_evaluator_agent()


class ResearchState(TypedDict):
    query: str
    research_answer: str
    evaluation: str
    score: float
    human_decision: str



async def research_node(state: ResearchState):
    response = await research_agent.ainvoke({
        "messages": [
            {"role": "user", "content": state["query"]}
        ]
    })

    return {
        "research_answer": response["messages"][-1].content
    }


async def evaluation_node(state: ResearchState):

    prompt = EVALUATION_USER_PROMPT.format(
        query=state["query"],
        research_response=state["research_answer"]
    )

    response = await evaluate_agent.ainvoke({
        "messages": [
            {"role": "user", "content": prompt}
        ]
    })

    raw = response["messages"][-1].content
    parsed = json.loads(raw)

    return {
        "evaluation": parsed.get("feedback"),
        "score": parsed.get("accuracy_score")
    }


async def human_check_node(state: ResearchState):

    score = state.get("score", 0)

    if score >= 18:
        return {"human_decision": "approve"}

    decision = interrupt({
        "message": "Low quality research. Approve or retry?",
        "score": score,
        "options": ["approve", "retry"]
    })

    return {"human_decision": decision}



def human_router(state: ResearchState):
    return "research_node" if state["human_decision"] == "retry" else END



graph = StateGraph(ResearchState)

graph.add_node("research_node", research_node)
graph.add_node("evaluation_node", evaluation_node)
graph.add_node("human_check_node", human_check_node)

graph.add_edge(START, "research_node")
graph.add_edge("research_node", "evaluation_node")
graph.add_edge("evaluation_node", "human_check_node")

graph.add_conditional_edges(
    "human_check_node",
    human_router,
    {
        "research_node": "research_node",
        END: END
    }
)

research_graph = graph.compile(checkpointer=checkpointer)