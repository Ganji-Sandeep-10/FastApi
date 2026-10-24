# Task Manager API

A simple REST API to create, read, update and delete tasks.
Built with FastAPI, Pydantic, SQLAlchemy 2.0 and SQLite.

## Install

1. Open a terminal in the project folder.
2. Install the packages:

```
pip install -r requirements.txt
```

## Start the server

Run this from the project folder (the one that contains the `app` folder):

```
uvicorn app.main:app --reload
```

The first time you start it, a file called `tasks.db` is created automatically
in the project folder, next to `app/`.
Your tasks are saved there, so they are still there after a restart.

## Test the API

Open http://127.0.0.1:8000/docs in your browser and use "Try it out",
or use Postman.

| Method | Path | What it does | Success code |
|---|---|---|---|
| POST | `/tasks` | Create a task | 201 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{task_id}` | Get one task | 200 |
| PATCH | `/tasks/{task_id}` | Update some fields of a task | 200 |
| DELETE | `/tasks/{task_id}` | Delete a task | 204 |

A missing task returns `404`. Invalid data returns `422`.

### Example: create a task

```json
{"title": "Learn FastAPI", "description": "Finish my first project"}
```

## Project files

- `app/main.py` - the API endpoints
- `app/database.py` - connection to `tasks.db` and database sessions
- `app/models.py` - the `tasks` table (SQLAlchemy)
- `app/schemas.py` - request and response rules (Pydantic)
- `app/__init__.py` - marks `app` as a Python package
- `requirements.txt` - the packages to install
- `tasks.db` - the database file (created automatically)
