from config.settings import LLM

def retrieval_agent(state):
    prompt = f"""
    You are a data assistant.
    From the following schema, return ONLY column names
    relevant to answering the question.

    Schema:
    {state['schema_context']}

    Question:
    {state['user_question']}
    """

    response = LLM.invoke(prompt)
    columns = [
        c.strip() for c in response.content.split(",")
    ]

    state["relevant_columns"] = columns
    return state
