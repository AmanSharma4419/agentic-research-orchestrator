from pydantic import BaseModel
from typing import List


class ResearchAnalysis(BaseModel):

    summary: str

    key_findings: List[str]

    trends: List[str]

    risks: List[str]