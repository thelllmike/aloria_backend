# schemas/order_item_schema.py

from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float

class OrderItemResponse(OrderItemCreate):
    order_item_id: int

    class Config:
        orm_mode: True
