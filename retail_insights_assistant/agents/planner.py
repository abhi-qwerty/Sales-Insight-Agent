from utils.llm_guard import guarded_llm_call

def planner_agent(state):
    prompt = f"""
You are a retail analytics planner.

Relevant columns:
{state['relevant_columns']}

Question:
{state['user_question']}

Extract intent as:
- metric
- filters
- group by
"""

    response = guarded_llm_call(state, prompt)

    # 🔁 FALLBACK (NO LLM)
    if response is None:
        state["planned_query"] = {
            "metric": "SUM(sales)",
            "group_by": ["category"],
            "filters": {}
        }
        return state

    state["planned_query"] = response
    return state
