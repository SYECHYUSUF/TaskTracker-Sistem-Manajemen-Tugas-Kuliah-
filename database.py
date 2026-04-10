import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Vercel's root filesystem is read-only, so we must use /tmp for SQLite if no external DB is found
is_vercel = os.getenv("VERCEL") == "1"
default_db_path = "sqlite:////tmp/tasktracker.db" if is_vercel else "sqlite:///./tasktracker.db"

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", default_db_path)

# SQLAlchemy 1.4+ requires "postgresql://" instead of "postgres://"
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()