from pydantic import BaseModel
from typing import Optional
from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float
    status: Optional[OrderStatus] = OrderStatus.pending

class OrderItemStatusUpdate(BaseModel):
    status: OrderStatus

class OrderItemResponse(OrderItemCreate):
    order_item_id: int

    class Config:
        orm_mode = True
