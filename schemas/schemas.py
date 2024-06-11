# schemas/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    customer = "customer"
    admin = "admin"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: Optional[UserRole] = UserRole.customer

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    created_at: datetime
    role: UserRole

    class Config:
        orm_mode: True

class AddressCreate(BaseModel):
    user_id: int
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str

class AddressResponse(AddressCreate):
    address_id: int
    created_at: datetime

    class Config:
        orm_mode: True
