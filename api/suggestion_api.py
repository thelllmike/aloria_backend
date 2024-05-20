# api/suggestion_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.suggestion_crud as crud
import schemas.suggestion_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/suggestions/", response_model=schemas.SuggestionResponse)
def create_suggestion(suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db)):
    return crud.create_suggestion(db=db, suggestion=suggestion)

@router.get("/suggestions/", response_model=list[schemas.SuggestionResponse])
def read_suggestions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suggestions = crud.get_suggestions(db, skip=skip, limit=limit)
    return suggestions

@router.get("/suggestions/{suggestion_id}", response_model=schemas.SuggestionResponse)
def read_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    suggestion = crud.get_suggestion(db, suggestion_id=suggestion_id)
    if suggestion is None:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return suggestion

@router.put("/suggestions/{suggestion_id}", response_model=schemas.SuggestionResponse)
def update_suggestion(suggestion_id: int, suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db)):
    db_suggestion = crud.get_suggestion(db, suggestion_id=suggestion_id)
    if db_suggestion is None:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return crud.update_suggestion(db=db, suggestion_id=suggestion_id, suggestion=suggestion)

@router.delete("/suggestions/{suggestion_id}", response_model=schemas.SuggestionResponse)
def delete_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    db_suggestion = crud.get_suggestion(db, suggestion_id=suggestion_id)
    if db_suggestion is None:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return crud.delete_suggestion(db=db, suggestion_id=suggestion_id)
