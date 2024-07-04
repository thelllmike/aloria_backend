from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float
    address_id: int

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: float
    order_date: datetime
    address_id: int

    class Config:
        orm_mode = True
