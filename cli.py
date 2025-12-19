from src.engine import DataEngine
from src.generator import QueryGenerator
from src.validator import QueryValidator

def main():
    print("CLI STARTED")
    csv = input("CSV path: ")
    engine = DataEngine(csv)
    engine.load()

    meta = engine.metadata()
    print("Columns:", meta["columns"])

    generator = QueryGenerator("data", meta["columns"])

    query = generator.select(
        cols=list(meta["columns"].keys())[:3],
        limit=5
    )

    safe_query = QueryValidator.validate(query)
    result = engine.execute(safe_query)
    print(result)

    engine.close()

if __name__ == "__main__":
    main()
