# schemas/order_schema.py

from pydantic import BaseModel
from datetime import datetime

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float
    address_id: int

class OrderResponse(OrderCreate):
    order_id: int
    order_date: datetime

    class Config:
        orm_mode: True
