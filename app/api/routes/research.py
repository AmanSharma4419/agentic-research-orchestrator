from fastapi import APIRouter

from app.schemas.research_request import ResearchRequest
from app.chains.research_chain import run_research_chain

router = APIRouter()


@router.post("/research")
async def research(request: ResearchRequest):

    result = await run_research_chain(request.query)

    return result