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


@app.post(
    "/tasks",
    status_code=201,
    summary="Create a task",
    description="Creates a task. The title is required and done starts as false.",
)
def create_task(task_data: TaskCreate):
    if task_data.title is None or not task_data.title.strip():
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required and cannot be empty"},
        )

    next_id = 1
    existing_ids = {task["id"] for task in tasks}
    while next_id in existing_ids:
        next_id += 1

    new_task = {
        "id": next_id,
        "title": task_data.title.strip(),
        "done": False,
    }
    tasks.append(new_task)

    return JSONResponse(status_code=201, content=new_task)


@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title, done value, or both for an existing task.",
)
def update_task(task_id: int, task_data: TaskUpdate):
    task_to_update = None

    for task in tasks:
        if task["id"] == task_id:
            task_to_update = task
            break

    if task_to_update is None:
        return task_not_found(task_id)

    update_data = task_data.model_dump(exclude_unset=True)

    if not update_data:
        return JSONResponse(
            status_code=400,
            content={"error": "Request body must contain title and/or done"},
        )

    if "title" in update_data:
        title = update_data["title"]
        if title is None or not title.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "Title cannot be empty"},
            )
        task_to_update["title"] = title.strip()

    if "done" in update_data:
        done = update_data["done"]
        if done is None:
            return JSONResponse(
                status_code=400,
                content={"error": "Done must be true or false"},
            )
        task_to_update["done"] = done

    return task_to_update
