import streamlit as st
import pandas as pd
from graph.state_graph import build_graph

st.set_page_config(page_title="Retail Insights Assistant")

st.title("🛍️ Retail Insights Assistant")

# ---------- Mode Selection ----------
ui_mode = st.radio("Select Mode", ["Summary", "Q&A"])
mode = "summary" if ui_mode == "Summary" else "qa"

# ---------- Reset Button ----------
if st.button("🔄 Reset State & Reload"):
    st.session_state.clear()
    st.rerun()

# ---------- File Upload ----------
uploaded = st.file_uploader(
    "Upload CSV / Excel / JSON",
    type=["csv", "xlsx", "json"]
)

if uploaded:
    # ---------- File Parsing ----------
    if uploaded.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded)
    elif uploaded.name.endswith(".json"):
        df = pd.read_json(uploaded)
    else:
        df = pd.read_csv(uploaded)

    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    graph = build_graph()

    # ---------- SUMMARY MODE ----------
    if mode == "summary":
        state = {
            "dataframe": df,
            "mode": "summary",
            "chat_history": [],
            "llm_calls": 0   # ✅ billing guard
        }

        result = graph.invoke(state)

        if result.get("summary"):
            st.success("Executive Summary")
            st.write(result["summary"])
        else:
            st.warning("No summary could be generated.")

    # ---------- Q&A MODE ----------
    else:
        question = st.text_input("Ask a business question")

        if question:
            state = {
                "dataframe": df,
                "user_question": question,
                "mode": "qa",
                "chat_history": [],
                "llm_calls": 0   # ✅ billing guard
            }

            result = graph.invoke(state)

            if result.get("query_result") is not None:
                st.subheader("Query Result")
                st.dataframe(result["query_result"])
            else:
                st.error("Unable to answer the question with available data.")
