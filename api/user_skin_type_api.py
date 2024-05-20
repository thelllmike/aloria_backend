# api/user_skin_type_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.user_skin_type_crud as crud
import schemas.user_skin_type_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user_skin_types/", response_model=schemas.UserSkinTypeResponse)
def create_user_skin_type(user_skin_type: schemas.UserSkinTypeCreate, db: Session = Depends(get_db)):
    return crud.create_user_skin_type(db=db, user_skin_type=user_skin_type)

@router.get("/user_skin_types/{user_id}", response_model=list[schemas.UserSkinTypeResponse])
def read_user_skin_types(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_skin_types = crud.get_user_skin_types(db, user_id=user_id, skip=skip, limit=limit)
    return user_skin_types

@router.get("/user_skin_types/item/{user_skin_type_id}", response_model=schemas.UserSkinTypeResponse)
def read_user_skin_type(user_skin_type_id: int, db: Session = Depends(get_db)):
    user_skin_type = crud.get_user_skin_type(db, user_skin_type_id=user_skin_type_id)
    if user_skin_type is None:
        raise HTTPException(status_code=404, detail="User skin type not found")
    return user_skin_type

@router.put("/user_skin_types/item/{user_skin_type_id}", response_model=schemas.UserSkinTypeResponse)
def update_user_skin_type(user_skin_type_id: int, user_skin_type: schemas.UserSkinTypeCreate, db: Session = Depends(get_db)):
    db_user_skin_type = crud.get_user_skin_type(db, user_skin_type_id=user_skin_type_id)
    if db_user_skin_type is None:
        raise HTTPException(status_code=404, detail="User skin type not found")
    return crud.update_user_skin_type(db=db, user_skin_type_id=user_skin_type_id, user_skin_type=user_skin_type)

@router.delete("/user_skin_types/item/{user_skin_type_id}", response_model=schemas.UserSkinTypeResponse)
def delete_user_skin_type(user_skin_type_id: int, db: Session = Depends(get_db)):
    user_skin_type = crud.get_user_skin_type(db, user_skin_type_id=user_skin_type_id)
    if user_skin_type is None:
        raise HTTPException(status_code=404, detail="User skin type not found")
    return crud.delete_user_skin_type(db=db, user_skin_type_id=user_skin_type_id)
