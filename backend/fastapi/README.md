# FastAPI Projects

This folder contains the shared FastAPI workspace for both FastAPI example apps. The Python virtual environment and dependency file are centralized here so both subprojects use the same environment.

## Shared Setup

From `backend/fastapi`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running a Project

After activating the shared virtual environment from `backend/fastapi`, start either app from its subfolder:

```bash
cd books-api
uvicorn main:app --reload
```

or:

```bash
cd database&auth
uvicorn main:app --reload
```

If you are still in the repository root, first run:

```bash
cd backend/fastapi
source venv/bin/activate
```

Then use one of the commands above.

Open the browser at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Projects

### books-api

A simple FastAPI book management API that demonstrates:

- path parameters and query parameters
- JSON request body handling
- in-memory create/read/update/delete operations
- filtering by category and author

### database&auth

A minimal FastAPI starter app with a simple root endpoint. It is intended as a foundation for adding:

- database models
- authentication and authorization
- more advanced request handling

## Dependencies

All Python dependencies are stored in `requirements.txt` at the root of this folder.

## Notes

- No separate `requirements.txt` is needed inside each subproject.
- Use the shared virtual environment located at `backend/fastapi/venv`.
- Run each app from its subfolder to keep import paths simple.
