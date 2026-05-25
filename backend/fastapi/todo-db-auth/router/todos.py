from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field

from models import Todos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

from .auth import get_current_user

router = APIRouter(
    tags=["todos"]
)

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
user_dependency = Annotated[dict, Depends(get_current_user)]
    # now user_dependency has info on user that the get_current_user provides


class TodoRequest(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=200)
    priority: int = Field(ge=1, le=5)
    complete: bool = False


@router.get("/")
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()



@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    
    todo_model = db.query(Todos)\
    .filter(Todos.id == todo_id)\
    .filter(Todos.owner_id == user.get('id'))\
    .first()
    # "\" only lets python know that the current line is being continued in next line
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail={"error": "Todo not found"})



@router.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,
                      db: db_dependency,
                      todo: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    
    todo_model = Todos(
        title=todo.title,
        description=todo.description,
        priority=todo.priority,
        complete=todo.complete,
        owner_id=user.get("id")
        #user.get("id") is coming from that user object thingy
        #user is AA pswd is AA for future use
    )
    db.add(todo_model)
    db.commit()
    return todo_model



@router.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,
                      db: db_dependency,
                      todo: TodoRequest = None,
                      todo_id: int = Path(gt=0)
                    ):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    
    todo_model = db.query(Todos)\
    .filter(Todos.id == todo_id)\
    .filter(Todos.owner_id == user.get('id'))\
    .first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    db.add(todo_model)
    db.commit()
    return None



@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency,
                      db: db_dependency,
                      todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail = "Authentication Failed")
    
    todo_model = db.query(Todos)\
    .filter(Todos.id == todo_id)\
    .filter(Todos.owner_id == user.get('id'))\
    .first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    
    db.query(Todos)\
    .filter(Todos.id == todo_id)\
    .filter(Todos.owner_id == user.get('id'))\
    .delete()
    
    db.commit()
    return None