from langgraph.graph import StateGraph, END
from models.state import AgentState

from agents.schema_discovery import schema_discovery_agent
from agents.retrieval_agent import retrieval_agent
from agents.planner import planner_agent
from agents.sql_engineer import sql_engineer_agent
from agents.validator import validator_agent
from agents.summarizer import summarizer_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("schema", schema_discovery_agent)
    graph.add_node("retrieve", retrieval_agent)
    graph.add_node("planner", planner_agent)
    graph.add_node("sql", sql_engineer_agent)
    graph.add_node("validator", validator_agent)
    graph.add_node("summary", summarizer_agent)

    graph.set_entry_point("schema")

    graph.add_conditional_edges(
        "schema",
        lambda s: s["mode"],
        {
            "summary": "summary",
            "qa": "retrieve"
        }
    )

    graph.add_edge("retrieve", "planner")
    graph.add_edge("planner", "sql")
    graph.add_edge("sql", "validator")

    graph.add_conditional_edges(
        "validator",
        lambda s: "retry" if s["error"] else END,
        {
            "retry": "sql",
            END: END
        }
    )

    graph.add_edge("summary", END)

    return graph.compile()
