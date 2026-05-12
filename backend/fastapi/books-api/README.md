# Books API

A FastAPI project that exposes a small in-memory book collection with read, filter, create, update, and delete operations.

## Features

- `GET /` returns a welcome message and points to `/books`
- `GET /books` returns all books
- `GET /books/{book_title}` returns a book by title (case-insensitive)
- `GET /books/?category={category}` filters books by category
- `GET /books/byauthor/?author={author}&category={category}` filters by author and category
- `POST /books/create_book` adds a new book from JSON request body
- `PUT /books/update_book` updates an existing book by title
- `DELETE /books/delete_book/{book_title}` removes a book by title

## Setup

```bash
cd backend/fastapi/books-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Notes

This project currently stores data in a Python list for demonstration purposes and is a good starting point for adding a real database or authentication logic.
