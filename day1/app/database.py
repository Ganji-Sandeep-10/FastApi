from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

class Base(DeclarativeBase):
    pass

# tasks.db always lives in the project root (the folder above app/),
# no matter which folder you start the server from.
BASE_DIR=Path(__file__).resolve().parent.parent
DATABASE_URL=f"sqlite:///{(BASE_DIR / 'tasks.db').as_posix()}"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
