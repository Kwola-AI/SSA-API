from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these with your MySQL credentials, database info, and port
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://kwola:j2sGzh9wBZoehJrkBx1lqDgeRFgjZQdf@dpg-cvocombuibrs73boa3m0-a:5432/ssa_db"

# Create the engine with the new MySQL URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Set up sessionmaker with no need for check_same_thread (SQLite-specific)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
