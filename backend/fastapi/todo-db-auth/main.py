from fastapi import FastAPI
import models
from database import engine

from router import auth, todos, admin, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine) 
# This line creates all the tables defined in your SQLAlchemy models in the database. 
# The create_all method is called on the metadata of the Base class, which is the base class for all your models. 
# The bind parameter specifies the database engine to use for creating the tables. 
# In this case, it uses the engine that was created in the database.py file, 
# which is connected to the SQLite database specified in the SQLALCHEMY_DATABASE_URL variable.

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)