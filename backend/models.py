from typing import Optional
from sqlmodel import SQLModel, Field, Session, create_engine
from fastapi import Depends

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    name: Optional[str] = None
    bio: Optional[str] = None


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = False
    priority: str = "medium"
    category: str = "general"
    important: bool = False
    created_at: Optional[str] = None
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
