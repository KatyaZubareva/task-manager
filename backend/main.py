from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from datetime import datetime

from models import Task, User, create_db_and_tables, get_session
from auth import create_access_token, get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:80", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_db_and_tables()

@app.post("/register")
def register(user: User, session: Session = Depends(get_session)):
    existing = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing:
        raise HTTPException(400, "User already exists")

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.email == form_data.username)
    ).first()

    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/api/tasks")
def get_tasks(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    return session.exec(
        select(Task).where(Task.user_id == user.id)
    ).all()


@app.post("/api/tasks")
def create_task(
    task: Task,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    task.user_id = user.id
    if not task.created_at:
        task.created_at = datetime.now().isoformat()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.put("/api/tasks/{task_id}")
def update_task(
    task_id: int,
    updated: Task,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    task = session.get(Task, task_id)

    if not task or task.user_id != user.id:
        raise HTTPException(404)

    task.title = updated.title
    task.description = updated.description
    task.completed = updated.completed
    task.priority = updated.priority
    task.category = updated.category
    task.important = updated.important

    session.add(task)
    session.commit()
    return task


@app.get("/api/tasks/{task_id}")
def get_task(
    task_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    task = session.get(Task, task_id)
    if not task or task.user_id != user.id:
        raise HTTPException(404)
    return task


@app.delete("/api/tasks/{task_id}")
def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    task = session.get(Task, task_id)

    if not task or task.user_id != user.id:
        raise HTTPException(404)

    session.delete(task)
    session.commit()
    return {"ok": True}
