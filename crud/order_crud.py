# crud/order_crud.py

from sqlalchemy.orm import Session
import models.order_model as models
import schemas.order_schema as schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.OrderModel).filter(models.OrderModel.user_id == user_id).offset(skip).limit(limit).all()

def get_order(db: Session, order_id: int):
    return db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()

def update_order(db: Session, order_id: int, order: schemas.OrderCreate):
    db_order = db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()
    if db_order:
        for key, value in order.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(models.OrderModel).filter(models.OrderModel.order_id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
