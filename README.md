# Task API — FlyRank Backend Track (Week 2, Assignment A1)

A small Task Management API built with **Python** and **FastAPI**. It supports creating, reading, updating, and deleting tasks.

## Requirements

- Python 3.10+
- pip

## Install and run

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install and start the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

## Interactive API documentation

Open **http://127.0.0.1:8000/docs** to see all endpoints and test them with Swagger UI's **Try it out** button.

Save a screenshot of the Swagger page as `docs/swagger.png` and include it in this repository before submitting.

## Endpoints

| Method | Endpoint | Description | Success status |
|---|---|---|---:|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{task_id}` | Get one task | 200 |
| POST | `/tasks` | Create a task | 201 |
| PUT | `/tasks/{task_id}` | Update a task | 200 |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 |

Errors:
- `400` — invalid request body or missing/empty title. The response contains an `error` message.
- `404` — task ID does not exist. The response contains an `error` message.

## Example requests

List tasks:

```bash
curl -i http://localhost:8000/tasks
```

Get one task:

```bash
curl -i http://localhost:8000/tasks/1
```

Create a task:

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
```

Update a task:

```bash
curl -i -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d '{"title":"Study FastAPI","done":true}'
```

Delete a task:

```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

An invalid create request such as `{}` returns `400`:

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{}'
```

## Example `curl -i` output

The exact headers can vary. A successful task-list request should include:

```text
HTTP/1.1 200 OK
content-type: application/json

[{"id":1,"title":"Study Python","done":false},{"id":2,"title":"Finish Assignment","done":false},{"id":3,"title":"Learn FastAPI","done":true}]
```

## Storage note

Tasks are stored in a Python list in memory. No database or file storage is used. The task list resets to the three example tasks whenever the server restarts.

## GitHub submission checklist

- [ ] Create a **public** GitHub repository.
- [ ] Commit the work as you complete the assignment stages (Stages 0–6); the assignment asks for at least 6 meaningful commits.
- [ ] Include this README, the endpoint table, a real `curl -i` output, and your Swagger screenshot.
- [ ] Push the commits to GitHub.
