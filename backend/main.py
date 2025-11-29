# main.py
# Main application routes (home, profile)
from typing import Union
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import User, Task, create_db_and_tables, get_session, SessionDep

app = FastAPI()

create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q: Union[str, None] = None):
    return {"task_id": task_id, "q": q}

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)