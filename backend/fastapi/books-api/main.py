from fastapi import FastAPI, Body

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



@app.get('/books/byauthor/')
async def read_author_category_by_query(author: str, category: str):
    #This endpoint allows us to filter books by both author and category using query parameters.
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



@app.post('/books/create_book')
async def create_book(new_book=Body()):
    #This endpoint allows us to create a new book by sending a JSON payload in the request body.
    #Body() is used to indicate that the new_book parameter should be read from the request body.
    BOOKS.append(new_book)
    return {"message": "Book created successfully.", "book": new_book}



@app.put('/books/update_book')
async def update_book(book_title: str, updated_book=Body()):
    #This endpoint allows us to update an existing book by sending a JSON payload in the request body.
    for i, book in enumerate(BOOKS):
        #enumerate() is used to get both the index and the book dictionary while iterating through the BOOKS list.
        #for i in range(len(BOOKS)) could also be used, but using enumerate() is more Pythonic and cleaner.
        #for i, book in BOOKS.items() would not work because BOOKS is a list, not a dictionary.
        if book.get('title').casefold() == book_title.casefold():
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully.", "book": updated_book}
    return {"message": "Book not found."}



@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    #This endpoint allows us to delete a book by its title using a path parameter.
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            deleted_book = BOOKS.pop(i)  #pop() is used to remove the book from the list and return it.
            return {"message": "Book deleted successfully.", "book": deleted_book}
    return {"message": "Book not found."}