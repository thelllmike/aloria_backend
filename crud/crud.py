from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime
import models.models as models, schemas.schemas as schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# address

def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict(), created_at=datetime.utcnow())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_addresses(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Address).filter(models.Address.user_id == user_id).offset(skip).limit(limit).all()

def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.address_id == address_id).first()

def update_address(db: Session, address_id: int, address: schemas.AddressCreate):
    user = get_user(db, address.user_id)
    if not user:
        raise ValueError(f"User with id {address.user_id} does not exist.")
    db_address = db.query(models.Address).filter(models.Address.address_id == address_id).first()
    if db_address:
        for key, value in address.dict().items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int):
    db_address = db.query(models.Address).filter(models.Address.address_id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address