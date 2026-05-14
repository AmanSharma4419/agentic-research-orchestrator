from pydantic import BaseModel
from typing import List


class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class ResearchResponse(BaseModel):
    query: str
    results: List[SearchResult]