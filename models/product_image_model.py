# models/product_image_model.py

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime
from database import Base

class ProductImageModel(Base):
    __tablename__ = "ProductImages"
    image_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('Products.product_id', ondelete='CASCADE'), nullable=False)
    image_url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)