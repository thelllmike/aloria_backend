# schemas/product_schema.py

from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    stock: int

class ProductResponse(ProductCreate):
    product_id: int

    class Config:
        orm_mode: True
