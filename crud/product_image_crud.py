# crud/product_image_crud.py

from sqlalchemy.orm import Session
import models.product_image_model as models
import schemas.product_image_schema as schemas

def create_product_image(db: Session, product_image: schemas.ProductImageCreate):
    db_product_image = models.ProductImageModel(**product_image.dict())
    db.add(db_product_image)
    db.commit()
    db.refresh(db_product_image)
    return db_product_image

def get_product_images(db: Session, product_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.ProductImageModel).filter(models.ProductImageModel.product_id == product_id).offset(skip).limit(limit).all()

def get_product_image(db: Session, image_id: int):
    return db.query(models.ProductImageModel).filter(models.ProductImageModel.image_id == image_id).first()

def update_product_image(db: Session, image_id: int, product_image: schemas.ProductImageCreate):
    db_product_image = db.query(models.ProductImageModel).filter(models.ProductImageModel.image_id == image_id).first()
    if db_product_image:
        for key, value in product_image.dict().items():
            setattr(db_product_image, key, value)
        db.commit()
        db.refresh(db_product_image)
    return db_product_image

def delete_product_image(db: Session, image_id: int):
    db_product_image = db.query(models.ProductImageModel).filter(models.ProductImageModel.image_id == image_id).first()
    if db_product_image:
        db.delete(db_product_image)
        db.commit()
    return db_product_image
