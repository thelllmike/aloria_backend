# crud/suggestion_crud.py

from sqlalchemy.orm import Session
import models.suggestion_model as models
import schemas.suggestion_schema as schemas

def create_suggestion(db: Session, suggestion: schemas.SuggestionCreate):
    db_suggestion = models.SuggestionModel(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

def get_suggestions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SuggestionModel).offset(skip).limit(limit).all()

def get_suggestion(db: Session, suggestion_id: int):
    return db.query(models.SuggestionModel).filter(models.SuggestionModel.suggestion_id == suggestion_id).first()

def update_suggestion(db: Session, suggestion_id: int, suggestion: schemas.SuggestionCreate):
    db_suggestion = db.query(models.SuggestionModel).filter(models.SuggestionModel.suggestion_id == suggestion_id).first()
    if db_suggestion:
        for key, value in suggestion.dict().items():
            setattr(db_suggestion, key, value)
        db.commit()
        db.refresh(db_suggestion)
    return db_suggestion

def delete_suggestion(db: Session, suggestion_id: int):
    db_suggestion = db.query(models.SuggestionModel).filter(models.SuggestionModel.suggestion_id == suggestion_id).first()
    if db_suggestion:
        db.delete(db_suggestion)
        db.commit()
    return db_suggestion
