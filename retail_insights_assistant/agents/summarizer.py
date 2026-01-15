from config.settings import LLM

def summarizer_agent(state):
    df = state["dataframe"]

    metrics = {
        "total_sales": df.select_dtypes("number").sum().to_dict(),
        "rows": len(df)
    }

    prompt = f"""
    You are an executive retail analyst.
    Create a concise performance summary.

    Metrics:
    {metrics}
    """

    response = LLM.invoke(prompt)
    state["summary"] = response.content
    return state
