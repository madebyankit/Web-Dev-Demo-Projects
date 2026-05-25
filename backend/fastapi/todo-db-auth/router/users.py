from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from models import Users
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Database session dependency for user routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inject current authenticated user and database session
# get_current_user is reused from auth.py for JWT validation.
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserVerification(BaseModel):
    # Request body for password update: current and new password
    password: str
    new_password: str = Field(min_length=6)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    # Return the authenticated user's record
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency,
                          user_verification: UserVerification):
    # Update the current user's password after verifying the old one
    # user_verification info is coming from req body and should match as defined by class above
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    # Confirm current password matches before changing it
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
    
@router.put("/phonenumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phonenumber(user:user_dependency, db:db_dependency,
                             phone_number: str):
  if user is None:
    raise HTTPException(status_code=401, detail='Authentication Failed')
  user_model = db.query(Users).filter(Users.id == user.get('id')).first()
  
  user_model.phone_number = phone_number
  db.add(user_model)
  db.commit()