# api/skintype_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.skintype_crud as crud
import schemas.skintype_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/skintypes/", response_model=schemas.SkinTypeResponse)
def create_skin_type(skin_type: schemas.SkinTypeCreate, db: Session = Depends(get_db)):
    return crud.create_skin_type(db=db, skin_type=skin_type)

@router.get("/skintypes/", response_model=list[schemas.SkinTypeResponse])
def read_skin_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skin_types = crud.get_skin_types(db, skip=skip, limit=limit)
    return skin_types

@router.get("/skintypes/{skin_type_id}", response_model=schemas.SkinTypeResponse)
def read_skin_type(skin_type_id: int, db: Session = Depends(get_db)):
    skin_type = crud.get_skin_type(db, skin_type_id=skin_type_id)
    if skin_type is None:
        raise HTTPException(status_code=404, detail="Skin type not found")
    return skin_type

@router.put("/skintypes/{skin_type_id}", response_model=schemas.SkinTypeResponse)
def update_skin_type(skin_type_id: int, skin_type: schemas.SkinTypeCreate, db: Session = Depends(get_db)):
    db_skin_type = crud.get_skin_type(db, skin_type_id=skin_type_id)
    if db_skin_type is None:
        raise HTTPException(status_code=404, detail="Skin type not found")
    return crud.update_skin_type(db=db, skin_type_id=skin_type_id, skin_type=skin_type)

@router.delete("/skintypes/{skin_type_id}", response_model=schemas.SkinTypeResponse)
def delete_skin_type(skin_type_id: int, db: Session = Depends(get_db)):
    db_skin_type = crud.get_skin_type(db, skin_type_id=skin_type_id)
    if db_skin_type is None:
        raise HTTPException(status_code=404, detail="Skin type not found")
    return crud.delete_skin_type(db=db, skin_type_id=skin_type_id)
