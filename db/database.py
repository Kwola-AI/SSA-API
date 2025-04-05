from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ PostgreSQL connection via psycopg2
DIRECT_URL="postgresql://postgres.lktwyssqcxwrajcwikvd:[asdf123]@aws-0-us-west-1.pooler.supabase.com:5432/ssa_db"



# Create engine
engine = create_engine(DIRECT_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
