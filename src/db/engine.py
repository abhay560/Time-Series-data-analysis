import os
from sqlalchemy import create_engine


DATABASE_URL = "MENTION YOUR BATABSE URL HERE"

def get_engine():
    return create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
