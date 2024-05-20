# crud/cart_crud.py

from sqlalchemy.orm import Session
import models.cart_model as models
import schemas.cart_schema as schemas

def create_cart_item(db: Session, cart_item: schemas.CartCreate):
    db_cart_item = models.CartModel(**cart_item.dict())
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def get_cart_items(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.CartModel).filter(models.CartModel.user_id == user_id).offset(skip).limit(limit).all()

def get_cart_item(db: Session, cart_id: int):
    return db.query(models.CartModel).filter(models.CartModel.cart_id == cart_id).first()

def update_cart_item(db: Session, cart_id: int, cart_item: schemas.CartCreate):
    db_cart_item = db.query(models.CartModel).filter(models.CartModel.cart_id == cart_id).first()
    if db_cart_item:
        for key, value in cart_item.dict().items():
            setattr(db_cart_item, key, value)
        db.commit()
        db.refresh(db_cart_item)
    return db_cart_item

def delete_cart_item(db: Session, cart_id: int):
    db_cart_item = db.query(models.CartModel).filter(models.CartModel.cart_id == cart_id).first()
    if db_cart_item:
        db.delete(db_cart_item)
        db.commit()
    return db_cart_item
