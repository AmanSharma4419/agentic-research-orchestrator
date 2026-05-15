from langchain.agents import create_agent
from app.services.llm_service import llm
from app.prompts.evaluation_prompt import EVALUATOR_SYSTEM_PROMPT

def build_evaluator_agent():
    agent = create_agent(
        model=llm,
        tools=[],
        system_prompt=EVALUATOR_SYSTEM_PROMPT
    )
    
    return agent
