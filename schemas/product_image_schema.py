# schemas/product_image_schema.py

from pydantic import BaseModel
from typing import Optional

class ProductImageCreate(BaseModel):
    product_id: int
    image_url: str

class ProductImageResponse(ProductImageCreate):
    image_id: int

    class Config:
        orm_mode: True