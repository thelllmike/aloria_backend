# models/order_item_model.py

from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from database import Base

class OrderItemModel(Base):
    __tablename__ = "OrderItems"
    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('Orders.order_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('Products.product_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
