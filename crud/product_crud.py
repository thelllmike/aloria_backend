# crud/product_crud.py

from sqlalchemy.orm import Session
import models.product_model as models
import schemas.product_schema as schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductModel).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.ProductModel).filter(models.ProductModel.product_id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.product_id == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.product_id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
