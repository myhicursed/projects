from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

DATABABASE_URL = "postgresql://postgres:myhicursed@localhost:5432/mhcmess"

engine = create_engine(DATABABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
