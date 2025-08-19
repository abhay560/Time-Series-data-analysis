import os
from sqlalchemy import create_engine

pwd = "Abhay%40"
DATABASE_URL = f"postgresql+psycopg2://postgres:{pwd}1999@localhost:5432/air_quality_db"

def get_engine():
    return create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
