# database.py

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv  

load_dotenv()

# Database configuration (PostgreSQL)
DATABASE_URL = os.getenv("DATABASE_URL")  

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()