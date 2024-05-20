# api/cart_api.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.cart_crud as crud
import schemas.cart_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cart/", response_model=schemas.CartResponse)
def create_cart_item(cart_item: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart_item(db=db, cart_item=cart_item)

@router.get("/cart/{user_id}", response_model=list[schemas.CartResponse])
def read_cart_items(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cart_items = crud.get_cart_items(db, user_id=user_id, skip=skip, limit=limit)
    return cart_items

@router.get("/cart/item/{cart_id}", response_model=schemas.CartResponse)
def read_cart_item(cart_id: int, db: Session = Depends(get_db)):
    cart_item = crud.get_cart_item(db, cart_id=cart_id)
    if cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return cart_item

@router.put("/cart/item/{cart_id}", response_model=schemas.CartResponse)
def update_cart_item(cart_id: int, cart_item: schemas.CartCreate, db: Session = Depends(get_db)):
    db_cart_item = crud.get_cart_item(db, cart_id=cart_id)
    if db_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return crud.update_cart_item(db=db, cart_id=cart_id, cart_item=cart_item)

@router.delete("/cart/item/{cart_id}", response_model=schemas.CartResponse)
def delete_cart_item(cart_id: int, db: Session = Depends(get_db)):
    db_cart_item = crud.get_cart_item(db, cart_id=cart_id)
    if db_cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return crud.delete_cart_item(db=db, cart_id=cart_id)
