from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.order_item_crud as crud
import schemas.order_item_schema as schemas
import database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order_items/", response_model=schemas.OrderItemResponse)
def create_order_item(order_item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_item(db=db, order_item=order_item)

@router.get("/order_items/{order_id}", response_model=list[schemas.OrderItemResponse])
def read_order_items(order_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_items = crud.get_order_items(db, order_id=order_id, skip=skip, limit=limit)
    return order_items

@router.get("/order_items/item/{order_item_id}", response_model=schemas.OrderItemResponse)
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    order_item = crud.get_order_item(db, order_item_id=order_item_id)
    if order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return order_item

@router.put("/order_items/item/{order_item_id}", response_model=schemas.OrderItemResponse)
def update_order_item(order_item_id: int, order_item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    db_order_item = crud.get_order_item(db, order_item_id=order_item_id)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return crud.update_order_item(db=db, order_item_id=order_item_id, order_item=order_item)

@router.delete("/order_items/item/{order_item_id}", response_model=schemas.OrderItemResponse)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    db_order_item = crud.get_order_item(db, order_item_id=order_item_id)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return crud.delete_order_item(db=db, order_item_id=order_item_id)


@router.put("/item/{order_item_id}/", response_model=schemas.OrderItemResponse)
def update_order_item_status(order_item_id: int, status_update: schemas.OrderItemStatusUpdate, db: Session = Depends(get_db)):
    db_order_item = crud.get_order_item(db, order_item_id=order_item_id)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return crud.update_order_item_status(db=db, order_item_id=order_item_id, status=status_update.status)