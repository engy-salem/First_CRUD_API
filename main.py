from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ConfigDict


app = FastAPI(
    title="Task API",
    version="1.0",
    description="A simple in-memory Task Management API built with FastAPI.",
)



# In-memory storage only. Tasks are reset when the server restarts.
tasks = [
    {"id": 1, "title": "Study Python", "done": False},
    {"id": 2, "title": "Finish Assignment", "done": False},
    {"id": 3, "title": "Learn FastAPI", "done": True},
]


class TaskCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Optional here so missing title can return the assignment's required 400,
    # rather than FastAPI's default 422.
    title: str | None = None


class TaskUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # PUT accepts title, done, or both.
    title: str | None = None
    done: bool | None = None



