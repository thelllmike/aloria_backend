# schemas/cart_schema.py

from pydantic import BaseModel
from datetime import datetime

class CartCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class CartResponse(CartCreate):
    cart_id: int
    added_at: datetime  # Change from str to datetime

    class Config:
        orm_mode: True
