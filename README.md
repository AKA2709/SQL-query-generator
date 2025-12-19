📊 CSV to SQL Analytics Engine

An interactive CSV analytics engine that allows users to upload CSV files and query them using SQL, powered by DuckDB and Streamlit.

This project bridges the gap between raw CSV data and SQL-based analytics by providing a safe, fast, and user-friendly querying interface.

🚀 Features

📁 Upload large CSV files

🧠 Automatic schema inference

⚡ In-memory analytics using DuckDB

🔐 Safe SQL execution (SELECT-only validation)

🛠 Auto SQL query generation

🖥 Interactive web UI with Streamlit

📊 Tabular results preview

🧩 Tech Stack

Python

DuckDB – fast in-memory analytical database

Streamlit – interactive web UI

Pandas – data handling

SQL

🏗 Project Architecture
SQL-query-generator/
├── src/
│   ├── engine.py        # DuckDB data engine
│   ├── generator.py     # SQL query builder
│   ├── validator.py     # SQL safety validation
│   └── __init__.py
├── app.py               # Streamlit application
├── cli.py               # CLI interface (optional)
├── requirements.txt
├── sample_data/
│   └── loan.csv
└── README.md

🧠 How It Works

User uploads a CSV file via the Streamlit UI

DuckDB loads the CSV into an in-memory table

Schema and row count are inferred automatically

User selects columns and row limits

SQL query is generated and validated

Query is executed and results are displayed

▶️ Running the Project Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/SQL-query-generator.git
cd SQL-query-generator

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run Streamlit app
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

🖥 Application Preview (What Users Can Do)

Upload a CSV file

View dataset metadata (rows & columns)

Select columns dynamically

Auto-generate SQL queries

Execute queries safely

View results in an interactive table

🔐 SQL Safety & Validation

To prevent unsafe operations:

Only SELECT and WITH queries are allowed

Multiple SQL statements are blocked

Destructive queries (DROP, DELETE, etc.) are rejected

This ensures safe analytics-only access.

📈 Why DuckDB?

Designed for analytical workloads

Faster than pandas for large CSV files

No external database setup required

SQL interface familiar to analysts

🎯 Use Cases

Data exploration for CSV datasets

SQL practice on real data

Lightweight analytics tool

Foundation for NL-to-SQL systems

Portfolio project for Data / AI roles

🛠 Future Improvements

🔍 Advanced filters (>, <, BETWEEN)

📊 Aggregations (GROUP BY, AVG, SUM)

🤖 Natural Language → SQL (LLM integration)

📉 Charts and dashboards

💾 Persistent database storage

📌 Resume-Ready Summary

Built an interactive CSV-to-SQL analytics engine using DuckDB and Streamlit, enabling safe SQL querying, schema inference, and real-time data exploration through a web interface.

👨‍💻 Author

Amrit Kalash
Aspiring Data / AI Engineer
Focused on building practical, production-ready analytics tools