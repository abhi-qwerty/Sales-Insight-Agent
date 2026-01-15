from utils.llm_guard import guarded_llm_call
from config.settings import DUCKDB_TABLE_NAME

def sql_engineer_agent(state):
    prompt = f"""
Generate DuckDB SQL.

Table: {DUCKDB_TABLE_NAME}
Allowed columns: {state['relevant_columns']}
Plan:
{state['planned_query']}
"""

    response = guarded_llm_call(state, prompt)

    if response is None:
        state["sql_query"] = f"""
        SELECT *
        FROM {DUCKDB_TABLE_NAME}
        LIMIT 10
        """
        return state

    sql = response.replace("```sql", "").replace("```", "")
    state["sql_query"] = sql
    return state
