def schema_discovery_agent(state):
    df = state["dataframe"]

    schema = []
    for col, dtype in df.dtypes.items():
        schema.append(f"{col} ({dtype})")

    state["schema_context"] = (
        "Available columns:\n" + "\n".join(schema)
    )
    return state
