# src/db/engine.py
import os
from sqlalchemy import create_engine

# read from env; fall back to a sensible local default
DATABASE_URL = "postgresql+psycopg2://postgres:Abhay%401999@localhost:5432/air_quality_db"

def get_engine():
    # future=True gives SQLA 2.0 style, pool_pre_ping avoids stale connections
    return create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
