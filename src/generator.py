class QueryGenerator:
    def __init__(self, table_name: str, columns: dict):
        self.table = table_name
        self.columns = columns

    def select(self, cols, where=None, limit=None):
        query = f"SELECT {', '.join(cols)} FROM {self.table}"

        if where:
            clauses = []
            for col, val in where.items():
                clauses.append(f"{col} = '{val}'")
            query += " WHERE " + " AND ".join(clauses)

        if limit:
            query += f" LIMIT {limit}"

        return query
