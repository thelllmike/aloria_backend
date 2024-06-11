# models/product_model.py

from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP
from datetime import datetime
from database import Base

class ProductModel(Base):
    __tablename__ = "Products"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    cost = Column(DECIMAL(10, 2), nullable=False)
    brand = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
