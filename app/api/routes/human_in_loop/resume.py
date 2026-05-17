from fastapi import APIRouter
from langgraph.types import Command

from app.graphs.research_graph import research_graph

router = APIRouter()


@router.post("/research/resume")
async def resume_graph(payload: dict):

    response = await research_graph.ainvoke(
        Command(
            resume=payload["decision"]
        ),
        config={
            "configurable": {
                "thread_id": payload["thread_id"]
            }
        }
    )

    return response