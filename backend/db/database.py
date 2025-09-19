from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your actual DSN or connection string
DATABASE_URL = "postgresql+psycopg2://postgres:sMc110499meNcp@127.0.0.1/pmd_dev"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
