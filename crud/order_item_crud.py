# crud/order_item_crud.py

from sqlalchemy.orm import Session
import models.order_item_model as models
import schemas.order_item_schema as schemas

def create_order_item(db: Session, order_item: schemas.OrderItemCreate):
    db_order_item = models.OrderItemModel(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

def get_order_items(db: Session, order_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItemModel).filter(models.OrderItemModel.order_id == order_id).offset(skip).limit(limit).all()

def get_order_item(db: Session, order_item_id: int):
    return db.query(models.OrderItemModel).filter(models.OrderItemModel.order_item_id == order_item_id).first()

def update_order_item(db: Session, order_item_id: int, order_item: schemas.OrderItemCreate):
    db_order_item = db.query(models.OrderItemModel).filter(models.OrderItemModel.order_item_id == order_item_id).first()
    if db_order_item:
        for key, value in order_item.dict().items():
            setattr(db_order_item, key, value)
        db.commit()
        db.refresh(db_order_item)
    return db_order_item

def delete_order_item(db: Session, order_item_id: int):
    db_order_item = db.query(models.OrderItemModel).filter(models.OrderItemModel.order_item_id == order_item_id).first()
    if db_order_item:
        db.delete(db_order_item)
        db.commit()
    return db_order_item
