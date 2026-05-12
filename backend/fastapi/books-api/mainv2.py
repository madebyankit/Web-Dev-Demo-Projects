from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


class Book:
    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: str):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest (BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create, it will be auto-generated", default=None)
    # Optional[int] means that the id field is optional and can be of type int. If not provided, it will default to None.
    
    title: str = Field(..., min_length=3, max_length=200)
    # ... means that the field is required and must be greater than 0, min_length and max_length are used to validate the length of the title.
    
    author: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    rating: int = Field(..., ge=1, le=5)
    published_date: Optional[str] = Field(..., min_length=1, max_length=100)

    model_config = {
        # The json_schema_extra field is used to provide additional information about the schema, 
        # such as an example of how the data should look when sent in a request.
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties.",
                "rating": 5,
                "published_date": "1925-04-10"
            }
        }
    }



BOOKS = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A novel set in the Roaring Twenties.", rating=5, published_date="1925-04-10"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="A novel about racial injustice in the Deep South.", rating=5, published_date="1960-07-11"),
    Book(id=3, title="1984", author="George Orwell", description="A dystopian novel about totalitarianism.", rating=4, published_date="1948-06-08"),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen", description="A classic romance novel.", rating=5, published_date="1813-01-28"),
    Book(id=5, title="The Catcher in the Rye", author="J.D. Salinger", description="A novel about teenage rebellion.", rating=4, published_date="1951-07-16"),
    Book(id=6, title="The Hobbit", author="J.R.R. Tolkien", description="A fantasy novel about a hobbit's adventure.", rating=5, published_date="1937-09-21")
]



@app.get("/books")
async def read_books(
    rating: Optional[int] = Query(None, ge=1, le=5, description="Filter books by rating (1-5)") ,
    published_date: Optional[str] = Query(None, description="Filter books by published date")
):
    # This endpoint can:
    # 1. Return all books if no query parameters are provided
    # 2. Filter books by rating
    # 3. Filter books by published date
    # 4. Filter books by both rating and published date together

    # Start with the full BOOKS list.
    # We will progressively filter this list based on the query parameters provided.
    filtered_books = BOOKS

    # Check if a rating query parameter was provided.
    # Example:
    # /books?rating=5
    if rating is not None:

        # Create a new list containing only books
        # whose rating matches the provided rating.
        filtered_books = [
            book for book in filtered_books
            if book.rating == rating
        ]

    # Check if a published_date query parameter was provided.
    # Example:
    # /books?published_date=1925-04-10
    if published_date is not None:

        # Further filter the existing filtered_books list
        # to only include books with the matching published date.
        filtered_books = [
            book for book in filtered_books
            if book.published_date == published_date
        ]

    # Convert each Book object into a dictionary using __dict__.
    # FastAPI can easily serialize dictionaries into JSON responses.
    return [book.__dict__ for book in filtered_books]



@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(ge=1, description="The ID of the book to retrieve")):
    # Path(ge=1) is extra validation that we are doing using Path, it ensures that the book_id provided in the path is greater than or equal to 1.
    for book in BOOKS:
        if book.id == book_id:
            return book.__dict__
    return {"message": "Book not found"}



@app.post("/create-book")
async def create_book(book_request: BookRequest): 
    #This endpoint allows us to create a new book by sending a POST request with the book details in the request body.
    new_book = Book(**book_request.dict())
    #The ** operator is used to unpack the dictionary returned by book_request.dict() and pass its key-value pairs as arguments to the Book constructor.
    BOOKS.append(find_book_id(new_book))
    return new_book



def find_book_id(book: Book):
    #This function assigns a unique ID to the new book by checking the last book in the BOOKS list and incrementing its ID by 1. If the BOOKS list is empty, it assigns an ID of 1 to the new book.
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return book



@app.put("/update-book/{book_id}")
async def update_book(new_book: BookRequest, book_id: int = Path(ge=1, description="The ID of the book to update")):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            # updated_book = Book(
            #     id=book_id,
            #     title=new_book.title,
            #     author=new_book.author,
            #     description=new_book.description,
            #     rating=new_book.rating
            # )
            updated_book = Book(
                id=book_id,
                **new_book.dict(exclude={"id"})
            )
            # The ** operator is used to unpack the dictionary returned by new_book.dict() 
            # and pass its key-value pairs as arguments to the Book constructor, along with the book_id for the id field.
            # The exclude={"id"} argument is used to exclude the id field from the dictionary, since we are providing it separately as book_id.

            BOOKS[index] = updated_book
            return updated_book.__dict__
    return {"message": "Book not found"}


@app.delete("/delete-book/{book_id}")
async def delete_book(book_id: int = Path(ge=1, description="The ID of the book to delete")):
    for index, book in enumerate(BOOKS):
        if book.id == book_id:
            del BOOKS[index]
            # The del statement is used to remove the book from the BOOKS list at the specified index. 
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}
    # for index in range(len(BOOKS)):
    #     if BOOKS[index].id == book_id:
    #         BOOKS.pop(index)
    #         return {"message": "Book deleted successfully"}
    # return {"message": "Book not found"}