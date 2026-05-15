from fastapi import APIRouter

from app.schemas.research_request import ResearchRequest
from app.agents.research_agent import run_research_agent

router = APIRouter()


@router.post("/agent-research")
async def agent_research(request: ResearchRequest):

    result = await run_research_agent(request.query)

    return result