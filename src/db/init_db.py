from pathlib import Path
from sqlalchemy import text
from src.db.engine import get_engine


SCHEMA_PATH = Path(__file__).resolve().parents[2] / "sql" / "schema.sql"

def init_db():
    ddl = SCHEMA_PATH.read_text(encoding="utf-8")
    engine = get_engine()
    with engine.begin() as conn:            
        conn.execute(text(ddl))
    print("Schema applied.")

if __name__ == "__main__":
    init_db()
