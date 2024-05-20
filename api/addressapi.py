# api/addressapi.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models, schemas.schemas as schemas, crud.crud as crud, database

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/addresses/", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)

@router.get("/addresses/{user_id}", response_model=list[schemas.AddressResponse])
def read_addresses(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db, user_id=user_id, skip=skip, limit=limit)
    return addresses

@router.get("/address/{address_id}", response_model=schemas.AddressResponse)
def read_address(address_id: int, db: Session = Depends(get_db)):
    address = crud.get_address(db, address_id=address_id)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.put("/address/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return crud.update_address(db=db, address_id=address_id, address=address)

@router.delete("/address/{address_id}", response_model=schemas.AddressResponse)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return crud.delete_address(db=db, address_id=address_id)


