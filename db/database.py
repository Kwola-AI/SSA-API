from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ PostgreSQL connection via psycopg2
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://kwola:j2sGzh9wBZoehJrkBx1lqDgeRFgjZQdf@dpg-cvocombuibrs73boa3m0-a:5432/ssa_db"
)

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
