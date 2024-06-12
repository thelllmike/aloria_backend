from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models
import schemas.product_schema as schemas
import schemas.product_image_schema as image_schemas
import crud.product_crud as product_cruds
import crud.product_image_crud as image_cruds
import database
import logging

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = product_cruds.create_product(db=db, product=product)
    logging.info(f"Product created with ID: {db_product.product_id}")
    return db_product

@router.get("/products/", response_model=List[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = product_cruds.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/products-mage/", response_model=List[schemas.ProductResponse])
def read_products_with_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = product_cruds.get_products(db, skip=skip, limit=limit)
    for product in products:
        product_images = image_cruds.get_product_images(db, product_id=product.product_id)
        product.images = product_images
    return products

@router.get("/products/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = product_cruds.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = product_cruds.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_cruds.update_product(db=db, product_id=product_id, product=product)

@router.put("/products/{product_id}/image", response_model=schemas.ProductResponse)
def update_product_and_image(product_id: int, product: schemas.ProductUpdate, image_url: str = Body(...), db: Session = Depends(get_db)):
    db_product = product_cruds.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_images = image_cruds.get_product_images(db, product_id=product_id)
    if not db_images:
        raise HTTPException(status_code=404, detail="Product image not found")

    # Update product
    updated_product = product_cruds.update_product(db=db, product_id=product_id, product=product)

    # Update product image (assuming a single image per product, adjust if necessary)
    updated_image = image_cruds.update_product_image(db=db, image_id=db_images[0].image_id, image_url=image_url)

    return updated_product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = product_cruds.get_product(db, product_id=product_id)  # Use cruds to call get_product
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    image_cruds.delete_product_images(db, product_id=product_id)
    product_cruds.delete_product(db, product_id=product_id)  # Use cruds to call delete_product
    return {"detail": "Product and associated images deleted"}
