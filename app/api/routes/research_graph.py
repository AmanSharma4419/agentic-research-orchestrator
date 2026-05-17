from fastapi import APIRouter
from app.graphs.research_graph import (research_graph)
from app.schemas.research_request import ResearchRequest

router = APIRouter(
    prefix="/api/v1/graph-research",
    tags=["LangGraph Research"]
)

@router.post("")
async def graph_research(payload:ResearchRequest):
    response = await research_graph.ainvoke(
        {
            "query":payload.query
            
        },
        config={
        "configurable": {
            "thread_id": payload.thread_id
        }
    }
    )
    return response