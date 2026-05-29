# Books API

A small FastAPI learning project for practicing REST-style routes, path parameters, query parameters, request bodies, validation, and HTTP status codes.

## Features

- Return an in-memory list of books
- Look up books by title or ID
- Filter books with query parameters
- Create, update, and delete books from the in-memory list
- Demonstrate request bodies with `Body`
- Demonstrate validation with Pydantic models, `Path`, and `Query`
- Return `HTTPException` errors for missing books in the advanced version

## Files

- `main.py` - introductory version using dictionaries and title-based routes
- `mainv2.py` - expanded version using a `Book` class, `BookRequest` Pydantic model, ID-based routes, validation, and status codes

## Getting Started

Use the shared Python environment from the parent FastAPI folder:

```bash
cd backend/fastapi
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the introductory API:

```bash
cd books-api
uvicorn main:app --reload
```

Run the expanded API instead:

```bash
cd books-api
uvicorn mainv2:app --reload
```

Open:

- App: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Example Routes

For `main.py`:

- `GET /`
- `GET /books`
- `GET /books/{book_title}`
- `GET /books/?category=science`
- `GET /books/byauthor/?author=Author Two&category=math`
- `POST /books/create_book`
- `PUT /books/update_book?book_title=Title One`
- `DELETE /books/delete_book/{book_title}`

For `mainv2.py`:

- `GET /books`
- `GET /books?rating=5`
- `GET /books?published_date=1925-04-10`
- `GET /books/{book_id}`
- `POST /create-book`
- `PUT /update-book/{book_id}`
- `DELETE /delete-book/{book_id}`

## Notes

- Data is stored in memory, so changes reset when the server restarts.
- This project does not use a database; use `todo-db-auth` for the database-backed FastAPI example.
