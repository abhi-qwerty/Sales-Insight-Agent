from typing import TypedDict, Optional, List
import pandas as pd

class AgentState(TypedDict):
    dataframe: Optional[pd.DataFrame]
    schema_context: Optional[str]
    relevant_columns: Optional[List[str]]

    user_question: Optional[str]
    mode: Optional[str]  

    planned_query: Optional[str]
    sql_query: Optional[str]

    query_result: Optional[pd.DataFrame]
    summary: Optional[str]

    chat_history: Optional[List[str]]  
    error: Optional[str]
    llm_calls: Optional[int]

