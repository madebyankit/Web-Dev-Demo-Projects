# FastAPI Database & Auth Demo

A minimal FastAPI starter application with a simple root endpoint. This project is intended as a base for adding database access and authentication.

## Features

- `GET /` returns a simple JSON greeting

## Setup

```bash
cd backend/fastapi/database&auth
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Notes

The current implementation is intentionally minimal. It is a good foundation for layering in database models, user authentication, and more advanced FastAPI functionality.
