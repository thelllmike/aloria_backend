# api/product_image_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.product_image_crud as crud
import schemas.product_image_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductImageResponse)
def create_product_image(product_image: schemas.ProductImageCreate, db: Session = Depends(get_db)):
    return crud.create_product_image(db=db, product_image=product_image)

@router.get("/product_images/", response_model=list[schemas.ProductImageResponse])
def read_product_images(product_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    product_images = crud.get_product_images(db, product_id=product_id, skip=skip, limit=limit)
    return product_images

@router.get("/product_images/{image_id}", response_model=schemas.ProductImageResponse)
def read_product_image(image_id: int, db: Session = Depends(get_db)):
    product_image = crud.get_product_image(db, image_id=image_id)
    if product_image is None:
        raise HTTPException(status_code=404, detail="Product image not found")
    return product_image

@router.put("/product_images/{image_id}", response_model=schemas.ProductImageResponse)
def update_product_image(image_id: int, product_image: schemas.ProductImageCreate, db: Session = Depends(get_db)):
    db_product_image = crud.get_product_image(db, image_id=image_id)
    if db_product_image is None:
        raise HTTPException(status_code=404, detail="Product image not found")
    return crud.update_product_image(db=db, image_id=image_id, product_image=product_image)

@router.delete("/product_images/{image_id}", response_model=schemas.ProductImageResponse)
def delete_product_image(image_id: int, db: Session = Depends(get_db)):
    db_product_image = crud.get_product_image(db, image_id=image_id)
    if db_product_image is None:
        raise HTTPException(status_code=404, detail="Product image not found")
    return crud.delete_product_image(db=db, image_id=image_id)