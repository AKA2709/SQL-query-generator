import streamlit as st
import pandas as pd
import tempfile

from src.engine import DataEngine
from src.generator import QueryGenerator
from src.validator import QueryValidator

st.set_page_config(page_title="CSV to SQL Analytics Engine", layout="wide")

st.title("📊 CSV → SQL Analytics Engine")
st.write("Upload a CSV file and query it using SQL (powered by DuckDB)")

# ---- Upload CSV ----
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        tmp.write(uploaded_file.getvalue())
        csv_path = tmp.name

    # Initialize engine
    engine = DataEngine(csv_path)
    engine.load()

    # Metadata
    meta = engine.metadata()

    st.subheader("📁 Dataset Metadata")
    st.write(f"**Rows:** {meta['rows']}")
    st.write("**Columns:**")
    st.json(meta["columns"])

    # Query builder
    st.subheader("🛠 Build SQL Query")

    selected_cols = st.multiselect(
        "Select columns",
        options=list(meta["columns"].keys()),
        default=list(meta["columns"].keys())[:3]
    )

    limit = st.number_input("Limit rows", min_value=1, max_value=1000, value=10)

    if st.button("Generate & Run Query"):
        generator = QueryGenerator("data", meta["columns"])
        query = generator.select(selected_cols, limit=limit)

        try:
            safe_query = QueryValidator.validate(query)
            st.code(safe_query, language="sql")

            result = engine.execute(safe_query)
            st.dataframe(result)

        except Exception as e:
            st.error(str(e))

    engine.close()
