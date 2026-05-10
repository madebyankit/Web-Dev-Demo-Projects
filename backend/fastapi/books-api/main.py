from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get('/')
async def root():
		return {"message": "Go to /books to see the list of books."}

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():  
            #casefold() is used to make the search case-insensitive
            #.get() is used to avoid KeyError if 'title' key is missing in any book dictionary
            return book
    return {"message": "Book not found."}

@app.get('/books/')
async def read_category_by_query(category: str):
    #This endpoint allows us to filter books by category using a query parameter.
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return