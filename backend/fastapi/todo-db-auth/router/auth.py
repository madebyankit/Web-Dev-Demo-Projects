from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette import status
from passlib.context import CryptContext

from models import Users
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import timedelta, datetime, timezone

from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

router = APIRouter()

SECRET_KEY = "b13f5431d3a117e2c41f7bb5f9e1ba118cd16edac13b2cad0b05e1bc6effcefe"
ALGORITHM = "HS256"
#this key can be anything, usually stored in .env, I generated it using terminal: openssl rand -hex 32

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
  username: str
  email: str
  first_name: str
  last_name: str
  password: str
  role: str  

class Token(BaseModel):
	access_token: str
	token_type: str
  
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


def authenticate_user(username:str, password:str, db):
  #Utility Function that checks whether user exists or not, if does check password
  #if authenticated return user, because we need this user info now to create JWT
  user = db.query(Users).filter(Users.username == username).first()
  if not user:
    return False
  if not bcrypt_context.verify(password, user.hashed_password):
    return False
  return user


def create_access_token(username: str,
                        user_id: int,
                        expires_delta: timedelta):
  #Utility to create JWT token
  encode = {'sub': username, 'id': user_id}
  expires = datetime.now(timezone.utc) + expires_delta
  encode.update({'exp': expires})
  return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request: CreateUserRequest):
  # create_user_request is coming from req body and is of type CreateUserRequest pydantic model 
  # then we use its values to initialise a create_user_model based on User Model from models
  # create_user_request = Users(**create_user_request.dict())
  # the abve approach won't work because pydantic model does not have hashed pswd and isactive etc
  create_user_model = Users(
		email=create_user_request.email,
  	username=create_user_request.username,
  	first_name=create_user_request.first_name,
		last_name=create_user_request.last_name,
		role=create_user_request.role,
		hashed_password=bcrypt_context.hash(create_user_request.password),
  	is_active=True
	)
  db.add(create_user_model)
  db.commit()
  return {"User Created Successfully" : create_user_model.username}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
  #just adding form_data: Annotated[...] now the route in swagger UI will take a lot more
  #input info regarding username, password
  user = authenticate_user(form_data.username, form_data.password, db)
  if not user:
    return "Failed Authenication"
  
  token = create_access_token(user.username, user.id, timedelta(minutes=20))
  return {"access_token": token, "token_type":"bearer"}