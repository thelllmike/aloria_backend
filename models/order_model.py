# models/order_model.py

from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey
from datetime import datetime
from database import Base

class OrderModel(Base):
    __tablename__ = "Orders"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    order_date = Column(TIMESTAMP, default=datetime.utcnow)
    address_id = Column(Integer, ForeignKey('Addresses.address_id', ondelete='CASCADE'), nullable=False)
