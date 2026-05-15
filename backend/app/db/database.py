# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration (PostgreSQL)
DATABASE_URL = "postgresql://postgres:1805@localhost:5432/resume_ai"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()