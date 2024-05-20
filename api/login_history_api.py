# api/login_history_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.login_history_crud as crud
import schemas.login_history_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login_history/", response_model=schemas.LoginHistoryResponse)
def create_login_history(login_history: schemas.LoginHistoryCreate, db: Session = Depends(get_db)):
    return crud.create_login_history(db=db, login_history=login_history)

@router.get("/login_history/{user_id}", response_model=list[schemas.LoginHistoryResponse])
def read_login_histories(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    login_histories = crud.get_login_histories(db, user_id=user_id, skip=skip, limit=limit)
    return login_histories

@router.get("/login_history/item/{login_id}", response_model=schemas.LoginHistoryResponse)
def read_login_history(login_id: int, db: Session = Depends(get_db)):
    login_history = crud.get_login_history(db, login_id=login_id)
    if login_history is None:
        raise HTTPException(status_code=404, detail="Login history not found")
    return login_history

@router.delete("/login_history/item/{login_id}", response_model=schemas.LoginHistoryResponse)
def delete_login_history(login_id: int, db: Session = Depends(get_db)):
    login_history = crud.get_login_history(db, login_id=login_id)
    if login_history is None:
        raise HTTPException(status_code=404, detail="Login history not found")
    return crud.delete_login_history(db=db, login_id=login_id)
