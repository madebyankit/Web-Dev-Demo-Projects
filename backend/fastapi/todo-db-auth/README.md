# Todo DB Auth

A FastAPI to-do application with database-backed users, JWT authentication, role-based admin routes, and server-rendered pages. It uses SQLAlchemy for models and sessions, PostgreSQL for the main database, Alembic for migrations, and Jinja templates for the browser UI.

## Features

- Register and log in users with hashed passwords
- Issue JWT bearer tokens for protected API routes
- Store users and to-dos in PostgreSQL
- Restrict normal users to their own to-dos
- Provide admin-only endpoints for viewing and deleting all to-dos
- Change user password and phone number
- Render login, registration, add, edit, and to-do list pages with Jinja2
- Run automated tests with FastAPI `TestClient` and a SQLite test database

## Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL with `psycopg2-binary`
- Alembic
- Jinja2 templates
- `python-jose` for JWTs
- `passlib` and bcrypt for password hashing
- Pytest

## Getting Started

Use the shared Python environment from the parent FastAPI folder:

```bash
cd backend/fastapi
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start PostgreSQL and create a database named `TodoApplicationDatabase`. The current local connection string is defined in `database.py` and `alembic.ini`:

```text
postgresql://postgres:anks1999@localhost/TodoApplicationDatabase
```

Update that value if your local PostgreSQL username, password, host, or database name is different.

Run the app from this project folder so template and static asset paths resolve correctly:

```bash
cd todo-db-auth
uvicorn main:app --reload
```

Open:

- App: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health check: `http://127.0.0.1:8000/healthy`

## Database and Migrations

The app calls `Base.metadata.create_all(bind=engine)` on startup, so tables can be created directly from the SQLAlchemy models during local development.

Alembic is also configured for schema migrations:

```bash
alembic upgrade head
```

`PostgreSQLScript.sql` contains a manual schema setup script, but it is older than the current model because the `Users` model now includes `phone_number`. Prefer the SQLAlchemy models and Alembic migration files when working with the current app.

## Tests

Run tests from `backend/fastapi/todo-db-auth`:

```bash
pytest
```

The tests use `test/utils.py` to create a SQLite test database named `testdb.db` and override the app dependencies used by route tests.

## Project Structure

```text
todo-db-auth/
├── alembic/              # Migration environment and versions
├── router/               # Auth, todo, user, and admin route modules
├── static/               # CSS and JavaScript for rendered pages
├── templates/            # Jinja2 HTML templates
├── test/                 # Pytest route and helper tests
├── database.py           # SQLAlchemy engine, session, and Base
├── main.py               # FastAPI app setup and router registration
├── models.py             # User and todo SQLAlchemy models
└── PostgreSQLScript.sql  # Manual schema reference
```

## Notes

- The JWT secret is currently hardcoded in `router/auth.py` for learning purposes. In a production app, move it to environment variables.
- The database URL is also hardcoded for a local PostgreSQL setup. Update it before running on another machine.
- Run `uvicorn` from this folder unless you also adjust the `templates` and `static` paths.
