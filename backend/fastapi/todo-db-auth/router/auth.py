#admin user is AA pswd is AA for future use
#normal user is AB pswd is AB

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from starlette import status
from passlib.context import CryptContext

from models import Users
from database import SessionLocal
# Type hints for dependency injection
from typing import Annotated
from sqlalchemy.orm import Session
# Date/time utilities for token expiration
from datetime import timedelta, datetime, timezone

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter(
	prefix = "/auth",  # All routes in this file will start with /auth
	tags=['auth']  # Groups routes in Swagger UI documentation
)

# JWT secret key - used to sign and verify JWT tokens (KEEP PRIVATE, store in .env)
# Generate with: openssl rand -hex 32
SECRET_KEY = "b13f5431d3a117e2c41f7bb5f9e1ba118cd16edac13b2cad0b05e1bc6effcefe"
# JWT algorithm for encoding/decoding tokens
ALGORITHM = "HS256"

# Create bcrypt password hashing context for secure password storage
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# OAuth2 scheme to extract token from Authorization header (Bearer token)
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

# Request body model for user registration
class CreateUserRequest(BaseModel):
  username: str
  email: str
  first_name: str
  last_name: str
  password: str
  role: str  

# Response model for login endpoint - returns the JWT token
class Token(BaseModel):
	access_token: str
	token_type: str
  
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the session to the request handler
    finally:
        db.close()  # Always close the session after the request completes

# Type annotation for database dependency - tells FastAPI to inject DB session via get_db()
db_dependency = Annotated[Session, Depends(get_db)]


# Verifies username and password during login
def authenticate_user(username:str, password:str, db):
  # Query database for user by username
  user = db.query(Users).filter(Users.username == username).first()
  if not user:
    return False  # User doesn't exist
  # Verify the provided password matches the stored hashed password
  if not bcrypt_context.verify(password, user.hashed_password):
    return False  # Password is incorrect
  return user  # Return user object if authentication succeeds


# Creates a signed JWT token containing user information
def create_access_token(username: str,
                        user_id: int,
                        role: str,
                        expires_delta: timedelta):
  # JWT payload - claims that will be encoded in the token
  # 'sub' = subject (standard claim, usually the username)
  # 'id' = custom claim to store user ID
  encode = {'sub': username, 'id': user_id, "role": role}
  # Calculate token expiration time
  expires = datetime.now(timezone.utc) + expires_delta
  # Add expiration claim ('exp') to the payload
  encode.update({'exp': expires})
  # Encode and sign the JWT using SECRET_KEY and ALGORITHM (HS256)
  # The token is cryptographically signed to prevent tampering
  return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# Validates the JWT token and extracts user information
# Called automatically by FastAPI when using db_dependency in protected routes
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        # Decode the JWT token using the SECRET_KEY
        # Verifies the signature hasn't been tampered with
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract claims from the decoded token
        username: str = payload.get('sub')  # Get username from 'sub' claim
        user_id: int = payload.get('id')  # Get user ID from custom 'id' claim
        user_role: str = payload.get('role')  # Get role if present
        # Verify required claims exist
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        # Return user info from token for use in protected endpoints
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        # Token is invalid, expired, or signature verification failed
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')



@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request: CreateUserRequest):
  # Create a new User model instance with data from the request body
  # Note: We map fields manually because CreateUserRequest doesn't include
  # database-specific fields like hashed_password and is_active
  create_user_model = Users(
		email=create_user_request.email,
  	username=create_user_request.username,
  	first_name=create_user_request.first_name,
		last_name=create_user_request.last_name,
		role=create_user_request.role,
		# Hash the plaintext password using bcrypt before storing
		hashed_password=bcrypt_context.hash(create_user_request.password),
  	is_active=True  # New users are active by default
	)
  # Add the new user to the database session
  db.add(create_user_model)
  # Commit the transaction to save the user to the database
  db.commit()
  return {"User Created Successfully" : create_user_model.username}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
  # OAuth2PasswordRequestForm expects username and password in form-data format
  # This is the standard OAuth2 login endpoint
  
  # Verify username and password against database
  user = authenticate_user(form_data.username, form_data.password, db)
  if not user:
    # Return 401 Unauthorized if credentials are invalid
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
  
  # Create a JWT token valid for 20 minutes
  token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
  # Return token in OAuth2 standard format (access_token and token_type)
  return {"access_token": token, "token_type":"bearer"}