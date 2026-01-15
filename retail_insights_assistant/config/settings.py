import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

LLM = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

DUCKDB_TABLE_NAME = "retail_data"
