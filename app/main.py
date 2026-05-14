from fastapi import FastAPI

from app.api.routes.research import router as research_router

app = FastAPI(
    title="Multi-Agent Research AI"
)

app.include_router(research_router)