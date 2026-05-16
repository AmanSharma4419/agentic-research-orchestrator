import json
from typing import TypedDict
from app.agents.builder_research_agent import build_research_agent
from app.agents.builder_evaluate_agent import build_evaluator_agent
from app.prompts.evaluation_prompt import EVALUATION_USER_PROMPT

from langgraph.graph import(StateGraph,START,END)

research_agent = build_research_agent()
evaluate_agent = build_evaluator_agent()

class ResearchState(TypedDict):
    query: str
    research_answer: str
    evaluation: dict
    retry_decision:str
    
async def research_node(state: ResearchState):
        response = await research_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )
        research_response = response["messages"][-1].content
        return {
                 "research_answer": research_response
              }
        
async def evaluation_node(
    state: ResearchState
):

    user_prompt = EVALUATION_USER_PROMPT.format(
        query=state.get("query"),
        research_response=state.get("research_answer")
    )

    evaluation_response = await evaluate_agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }
    )

    raw_evaluation_response = (
        evaluation_response["messages"][-1].content
    )
    final_evaluation_response = json.loads(raw_evaluation_response)
    
    return {
        "evaluation": final_evaluation_response
    }
      
async def should_retry_node(state:ResearchState):
       evaluation = state["evaluation"]
       print(evaluation,"evvv")
       if evaluation["needs_retry"]:
           return {
               "retry_decision": "retry"
           }      
       return {
        "retry_decision": "complete"
    }
     
def retry_router(state:ResearchState):
    return state["retry_decision"]

  
graph_builder = StateGraph(ResearchState)

graph_builder.add_node("research_node",research_node)
graph_builder.add_node("evaluation_node",evaluation_node)
graph_builder.add_node("should_retry_node",should_retry_node)

graph_builder.add_edge(START,"research_node")
graph_builder.add_edge("research_node","evaluation_node")
graph_builder.add_edge("evaluation_node","should_retry_node")

graph_builder.add_edge("evaluation_node",END)
graph_builder.add_conditional_edges(
    "should_retry_node",
    retry_router,
    {
        "retry": "research_node",
        "complete": END
    }
)
research_graph = graph_builder.compile()