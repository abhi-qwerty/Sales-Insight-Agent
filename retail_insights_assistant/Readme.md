# 🛍️ Retail Insights Assistant

## 📌 Overview
The Retail Insights Assistant is a GenAI-powered analytics application that allows business users and analysts to explore retail sales data using natural language.
Unlike traditional dashboards or static reports, this system dynamically understands the structure of uploaded data, generates SQL queries on the fly, validates results, and produces accurate, explainable insights — all while being designed to scale to 100GB+ datasets.
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-v0.3-green)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

---
## 🎯 Key Capabilities
The system uses an : **Multi-agent GenAI orchestration** **SQL-based analytics** 
**Cost-controlled LLM usage** and **Scalable data architecture design**

1.  **📊 Upload sales data (CSV / Excel / JSON)**
2.  **🧠 Ask analytical questions in plain English**
3.  **🧾 Generate executive summaries automatically**
4.  **🔁 Self-correct SQL errors dynamically**
5.  **💸 Built-in LLM cost guardrails**
---
## 🧠 Main Overview
### 🧩 Supported Use Cases
**1️⃣ Summarization Mode**
Generates a concise, human-readable executive summary of overall sales performance.

Example Output: “Overall sales increased steadily, with the West region leading revenue contribution. High-performing categories include Electronics and Apparel.”

**2️⃣ Conversational Q&A Mode**
Ask ad-hoc analytical questions using natural language without knowing SQL.
Example Queries:

1. “Which category had the highest sales in the North region?”
2. “Which product line underperformed in Q4?”
3. “Show top 5 regions by revenue.”

Accuracy Guarantee: All answers are backed by real SQL execution on the uploaded data, eliminating LLM hallucinations.

---
## 📂 System Architecture

### High-Level Flow
```text
User Input (CSV / Excel / JSON)
        ↓
Schema Discovery Agent
        ↓
Retrieval Agent (Relevant Columns)
        ↓
Planner Agent (NL → Query Intent)
        ↓
SQL Engineer Agent
        ↓
Validator Agent (Execution + Retry)
        ↓
Result / Summary
```
### Multi-Agent Design (LangGraph)
```text
| Agent            | Responsibility                     |
| ---------------- | ---------------------------------- |
| Schema Discovery | Understand columns & data types    |
| Retrieval Agent  | Select relevant columns (RAG-lite) |
| Planner Agent    | Convert NL → analytical intent     |
| SQL Engineer     | Generate DuckDB SQL                |
| Validator        | Execute SQL & handle errors        |
| Summarizer       | Generate executive summary         |

```

### 🧠 LLM Integration

**Model**: gemini-2.5-flash-lite
**Framework**: LangGraph + LangChain Google GenAI
**Prompt Engineering**: Structured prompts per agent
**Memory**: Maintained via LangGraph state
**Cost Control**: Max 2 LLM calls per request

### 💸 Cost Guardrail Strategy

To prevent unexpected billing:
**Each request tracks llm_calls**
**After 2 LLM calls, system falls back to deterministic logic**
**No infinite retries or runaway prompts**

---
## 📂 Project Structure

```text
retail_insights_assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── config/
│   └── settings.py
│
├── agents/
│   ├── schema_discovery.py
│   ├── retrieval_agent.py
│   ├── planner.py
│   ├── sql_engineer.py
│   ├── validator.py
│   └── summarizer.py
│
├── graph/
│   └── state_graph.py
│
├── db/
│   └── duckdb_manager.py
│
├── models/
│   └── state.py
│
├── utils/
    └── llm_guard.py


```


## ▶️ How to Run

### 1. Prerequisites

Make sure you have the following installed and configured:

- Python **3.11+**
- Google API Key
---

### 2. Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/abhi-qwerty/retail_insight_assistant.git
cd retail_insight_assistant
python -m venv venv
pip install -r requirements.txt
```
---

### 3. Add relevent API Keys in .env file
```text
GOOGLE_API_KEY=your_google_api_key
```
---

## 4. ▶️ Run the Agent

Start the Streamlit application using the following command:

```bash
streamlit run app.py
```

Once the application starts, Streamlit will display a local URL in the terminal (usually):

```bash
http://localhost:8501
```
## 🧠 What You Can Do

### 🌦 Select mode from the UI either Summary or Q&A and then upload sales data (.csv,.xlsx,.json)
The agent can give summary on real-time sales data you provide.
* **Example:** *"What is the revenue in Q2?"*

Upload any PDF document through the user interface to chat with your sales data.
* **Upload:** Upload your PDF file and see the few sample uploaded data frames for validation.
* **Ask:** Ask questions related to the specific content of the uploaded sales file.
* **Result:** The AI retrieves the data from database by executing sql queries to provide accurate answers.

---
