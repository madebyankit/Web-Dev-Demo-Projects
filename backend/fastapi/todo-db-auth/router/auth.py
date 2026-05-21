from fastapi import APIRouter
from pydantic import BaseModel
from passlib.context import CryptContext

from models import Users

router = APIRouter()
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
  username: str
  email: str
  first_name: str
  last_name: str
  password: str
  role: str  

@router.post("/auth/")
async def create_user(create_user_request: CreateUserRequest):
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
  return create_user_model