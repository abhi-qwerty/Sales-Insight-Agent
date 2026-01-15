from config.settings import LLM

MAX_LLM_CALLS = 1

def guarded_llm_call(state, prompt: str):
    """
    Makes an LLM call only if call limit not exceeded.
    """
    calls = state.get("llm_calls", 0)

    if calls >= MAX_LLM_CALLS:
        return None  # Trigger fallback

    response = LLM.invoke(prompt)
    state["llm_calls"] = calls + 1
    return response.content
