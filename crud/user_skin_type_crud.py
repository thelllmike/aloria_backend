# crud/user_skin_type_crud.py

from sqlalchemy.orm import Session
import models.user_skin_type_model as models
import schemas.user_skin_type_schema as schemas

def create_user_skin_type(db: Session, user_skin_type: schemas.UserSkinTypeCreate):
    db_user_skin_type = models.UserSkinTypeModel(**user_skin_type.dict())
    db.add(db_user_skin_type)
    db.commit()
    db.refresh(db_user_skin_type)
    return db_user_skin_type

def get_user_skin_types(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.UserSkinTypeModel).filter(models.UserSkinTypeModel.user_id == user_id).offset(skip).limit(limit).all()

def get_user_skin_type(db: Session, user_skin_type_id: int):
    return db.query(models.UserSkinTypeModel).filter(models.UserSkinTypeModel.user_skin_type_id == user_skin_type_id).first()

def update_user_skin_type(db: Session, user_skin_type_id: int, user_skin_type: schemas.UserSkinTypeCreate):
    db_user_skin_type = db.query(models.UserSkinTypeModel).filter(models.UserSkinTypeModel.user_skin_type_id == user_skin_type_id).first()
    if db_user_skin_type:
        for key, value in user_skin_type.dict().items():
            setattr(db_user_skin_type, key, value)
        db.commit()
        db.refresh(db_user_skin_type)
    return db_user_skin_type

def delete_user_skin_type(db: Session, user_skin_type_id: int):
    db_user_skin_type = db.query(models.UserSkinTypeModel).filter(models.UserSkinTypeModel.user_skin_type_id == user_skin_type_id).first()
    if db_user_skin_type:
        db.delete(db_user_skin_type)
        db.commit()
    return db_user_skin_type
