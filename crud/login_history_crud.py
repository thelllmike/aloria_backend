# crud/login_history_crud.py

from sqlalchemy.orm import Session
import models.login_history_model as models
import schemas.login_history_schema as schemas

def create_login_history(db: Session, login_history: schemas.LoginHistoryCreate):
    db_login_history = models.LoginHistoryModel(**login_history.dict())
    db.add(db_login_history)
    db.commit()
    db.refresh(db_login_history)
    return db_login_history

def get_login_histories(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.LoginHistoryModel).filter(models.LoginHistoryModel.user_id == user_id).offset(skip).limit(limit).all()

def get_login_history(db: Session, login_id: int):
    return db.query(models.LoginHistoryModel).filter(models.LoginHistoryModel.login_id == login_id).first()

def delete_login_history(db: Session, login_id: int):
    db_login_history = db.query(models.LoginHistoryModel).filter(models.LoginHistoryModel.login_id == login_id).first()
    if db_login_history:
        db.delete(db_login_history)
        db.commit()
    return db_login_history
