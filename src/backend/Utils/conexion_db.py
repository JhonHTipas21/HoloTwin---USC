from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Direct database configuration
DATABASE_URL = "postgresql://postgres:jhon2003@localhost:5432/holotwindb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()