from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .product_image_schema import ProductImageResponse

class ProductCreate(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    stock: int
    category: str
    cost: float
    brand: str

class ProductUpdate(ProductCreate):
    pass

class ProductResponse(ProductCreate):
    product_id: int
    created_at: datetime
    images: List[ProductImageResponse] = []

    class Config:
        orm_mode = True
