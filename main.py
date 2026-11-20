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



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid request body"},
    )


def task_not_found(task_id: int):
    return JSONResponse(
        status_code=404,
        content={"error": f"Task {task_id} not found"},
    )


@app.get(
    "/",
    summary="API information",
    description="Returns the name, version, and main endpoint of the API.",
)
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


@app.get(
    "/health",
    summary="Health check",
    description="Checks whether the API server is running.",
)
def health_check():
    return {"status": "ok"}


@app.get(
    "/tasks",
    summary="List all tasks",
    description="Returns all tasks stored in memory.",
)
def get_tasks():
    return tasks


@app.get(
    "/tasks/{task_id}",
    summary="Get one task",
    description="Returns one task by its ID, or a 404 error if it does not exist.",
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return task_not_found(task_id)


