# Task Management API


A RESTful API built with **Python** and **FastAPI** to create, retrieve, update, and delete tasks.

## Requirements

- Python 3.10+
- pip

## Installation and Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## Interactive API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Use the **Try it out** button to test the API endpoints directly from your browser.

Before submitting the assignment, save a screenshot of the Swagger documentation as:

`docs/swagger.png`

## API Endpoints

| Method | Endpoint | Description | Success Status |
|---|---|---|---:|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{task_id}` | Get one task by ID | 200 |
| POST | `/tasks` | Create a new task | 201 |
| PUT | `/tasks/{task_id}` | Update an existing task | 200 |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 |

### Error Responses

The API handles the following errors:

- **400 Bad Request:** Returned when the request body is invalid or the task title is missing or empty. The response contains an `error` message.
- **404 Not Found:** Returned when the requested task ID does not exist. The response contains an `error` message.

## Example Requests

The following examples use `curl` to interact with the API.

### 1. List all tasks

```bash
curl -i http://localhost:8000/tasks
```

### 2. Get one task

```bash
curl -i http://localhost:8000/tasks/1
```

### 3. Create a new task

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
```

### 4. Update an existing task

```bash
curl -i -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d '{"title":"Study FastAPI","done":true}'
```

### 5. Delete a task

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

### 6. Test an invalid create request

An empty request body should return a `400 Bad Request` response.

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{}'
```

## Example curl Output

Paste an actual `curl -i` response from your running API here before submitting.

For example, a successful request to list all tasks should return an HTTP `200 OK` response with a JSON array of tasks.

## Storage

Tasks are stored in a Python list in memory.

- No database is used.
- No file storage is used.
- The task list resets to the three example tasks whenever the server restarts.

## Project Structure

```text
First_CRUD_API/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    └── swagger.png
```

## GitHub Submission Checklist

- [ ] Create a public GitHub repository.
- [ ] Make at least 6 meaningful commits while completing the assignment stages (Stages 0–6).
- [ ] Include this README file.
- [ ] Include the API endpoints table.
- [ ] Include actual `curl -i` output.
- [ ] Include a Swagger UI screenshot at `docs/swagger.png`.
- [ ] Push all commits to GitHub.
