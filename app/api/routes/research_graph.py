import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.graphs.research_graph import (research_graph)
from app.schemas.research_request import ResearchRequest

router = APIRouter(
    prefix="/api/v1/graph-research",
    tags=["LangGraph Research"]
)

@router.post("/research/stream")
async def stream_research(query: str):

    async def event_generator():

        inputs = {
            "query": query,
            "research_answer": "",
            "evaluation": "",
            "retry_decision": ""
        }

        async for event in research_graph.astream(inputs):

            print("NODE EVENT:", event)

            yield json.dumps(event) + "\n"

    return StreamingResponse(event_generator(), media_type="text/plain")