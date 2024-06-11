from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models
import schemas.product_schema as schemas
import crud.product_crud as cruds
import crud.product_image_crud as crud
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
    db_product = crud.create_product(db=db, product=product)
    logging.info(f"Product created with ID: {db_product.product_id}")
    return db_product

@router.get("/products/", response_model=list[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/products-mage/", response_model=List[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = cruds.get_products(db, skip=skip, limit=limit)
    for product in products:
        product_images = crud.get_product_images(db, product_id=product.product_id)
        product.images = product_images
    return products

@router.get("/products/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product_id=product_id, product=product)



@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = cruds.get_product(db, product_id=product_id)  # Use cruds to call get_product
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    crud.delete_product_images(db, product_id=product_id)
    cruds.delete_product(db, product_id=product_id)  # Use cruds to call delete_product
    return {"detail": "Product and associated images deleted"}