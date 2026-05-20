from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field

from models import Todos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    # In this context, the finally block ensures that the database session is closed after it has been used, 
    # regardless of whether an exception occurred or not. 
    # The get_db function is a generator function that yields a database session. 
    # When the function is called, it creates a new session and yields it to the caller. 
    # After the caller is done using the session, the finally block is executed, 
    # which closes the session to free up resources and prevent potential memory leaks.

db_dependency = Annotated[Session, Depends(get_db)]
    # db:db_dependency is a parameter that indicates that the db variable is of type Session 
    # and is obtained from the get_db function using FastAPI's dependency injection system.


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=200)
    priority: int = Field(ge=1, le=5)
    completed: bool = False


@router.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()  



@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail={"error": "Todo not found"})



@router.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo: TodoRequest):
    todo_model = Todos(
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        completed=todo.completed
    )
    db.add(todo_model)
    db.commit()
    return todo_model



@router.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                        todo: TodoRequest = None ,
                        todo_id: int = Path(gt=0)
                    ):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.completed = todo.completed
    
    db.add(todo_model)
    db.commit()
    return None



@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    return None