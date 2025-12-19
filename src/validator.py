import re

class QueryValidator:
    @staticmethod
    def validate(query: str):
        query = re.sub(r"\s+", " ", query.strip())
        if not query.lower().startswith(("select", "with")):
            raise ValueError("Only SELECT queries allowed")
        if ";" in query:
            raise ValueError("Multiple statements not allowed")
        return query
