from fastapi import FastAPI, Request, status
from models import Base
from database import engine

from router import auth, todos, admin, users

from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine) 
# This line creates all the tables defined in your SQLAlchemy models in the database. 
# The create_all method is called on the metadata of the Base class, which is the base class for all your models. 
# The bind parameter specifies the database engine to use for creating the tables. 
# In this case, it uses the engine that was created in the database.py file, 
# which is connected to the SQLite database specified in the SQLALCHEMY_DATABASE_URL variable.

app.mount("/static", StaticFiles(directory="static"), name="static")

# app.mount("/static", StaticFiles(directory="todo-db-auth/static"), name="static")
# path is important, first path when venv is inside fastapi and uvicorn running from inside todo-db-auth already
# if uvicorn running from fastapi then use this commented path, same goes for other relative path depending on where we run server from
# we may need to update paths


@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)