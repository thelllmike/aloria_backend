# crud/skintype_crud.py

from sqlalchemy.orm import Session
import models.skintype_model as models
import schemas.skintype_schema as schemas

def create_skin_type(db: Session, skin_type: schemas.SkinTypeCreate):
    db_skin_type = models.SkinTypeModel(**skin_type.dict())
    db.add(db_skin_type)
    db.commit()
    db.refresh(db_skin_type)
    return db_skin_type

def get_skin_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SkinTypeModel).offset(skip).limit(limit).all()

def get_skin_type(db: Session, skin_type_id: int):
    return db.query(models.SkinTypeModel).filter(models.SkinTypeModel.skin_type_id == skin_type_id).first()

def update_skin_type(db: Session, skin_type_id: int, skin_type: schemas.SkinTypeCreate):
    db_skin_type = db.query(models.SkinTypeModel).filter(models.SkinTypeModel.skin_type_id == skin_type_id).first()
    if db_skin_type:
        for key, value in skin_type.dict().items():
            setattr(db_skin_type, key, value)
        db.commit()
        db.refresh(db_skin_type)
    return db_skin_type

def delete_skin_type(db: Session, skin_type_id: int):
    db_skin_type = db.query(models.SkinTypeModel).filter(models.SkinTypeModel.skin_type_id == skin_type_id).first()
    if db_skin_type:
        db.delete(db_skin_type)
        db.commit()
    return db_skin_type
