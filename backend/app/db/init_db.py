# init_db.py

from app.db.database import engine
from app.db.models import Base

# This file is responsible for initializing the database and creating tables if they don't exist.
def init_db():
    print(" Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
    print(" Done")

if __name__ == "__main__":
    init_db()