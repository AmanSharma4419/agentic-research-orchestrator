from fastapi import FastAPI

from app.api.routes.research import router as research_router
from app.api.routes.agent_research import router as agent_research_router
from app.api.routes.research_graph import (
    router as research_graph_router
)
app = FastAPI(
    title="Multi-Agent Research AI"
)

app.include_router(research_router)
app.include_router(agent_research_router)
app.include_router(research_graph_router)
