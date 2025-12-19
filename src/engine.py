import duckdb
import logging

class DataEngine:
    def __init__(self, csv_path: str, table_name="data"):
        self.csv_path = csv_path
        self.table_name = table_name
        self.con = duckdb.connect(":memory:")

    def load(self):
        self.con.execute(f"""
            CREATE TABLE {self.table_name} AS
            SELECT * FROM read_csv_auto('{self.csv_path}', header=True)
        """)

    def execute(self, query: str):
        return self.con.execute(query).fetchdf()

    def metadata(self):
        result = self.con.execute(
            f"DESCRIBE {self.table_name}"
        )
        cols = result.fetchall()
        result = self.con.execute(
            f"SELECT COUNT(*) FROM {self.table_name}"
        )
        row = result.fetchone()
        count = row[0] if row is not None else 0
        return {
            "columns": {c[0]: c[1] for c in cols},
            "rows": count
        }

    def close(self):
        self.con.close()
