from db.duckdb_manager import DuckDBManager

def validator_agent(state):
    db = DuckDBManager()
    db.register_dataframe(state["dataframe"])

    try:
        result = db.execute(state["sql_query"])
        state["query_result"] = result
        state["error"] = None
    except Exception as e:
        state["error"] = str(e)
        state["query_result"] = None

    return state
