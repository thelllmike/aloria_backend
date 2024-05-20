# models/cart_model.py

from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from database import Base

class CartModel(Base):
    __tablename__ = "Cart"
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('Products.product_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    added_at = Column(TIMESTAMP, default=datetime.utcnow)
