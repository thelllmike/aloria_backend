# api/userapi.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models, schemas.schemas as schemas, crud.crud as crud, database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.UserResponse)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# New endpoint to save email from Google sign-in
@router.post("/save_email/")
def save_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user:
        return {"message": "Email already registered"}
    new_user = schemas.UserCreate(
        username=email.split('@')[0],  # Creating a username from email prefix
        email=email,
        password="default_password",  # Default password
        role='customer'  # Default role
    )
    created_user = crud.create_user(db=db, user=new_user)
    return {"message": "Email saved successfully", "user": created_user}