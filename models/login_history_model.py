# models/login_history_model.py

from sqlalchemy import Column, Integer, TIMESTAMP, String, ForeignKey
from datetime import datetime
from database import Base

class LoginHistoryModel(Base):
    __tablename__ = "LoginHistory"
    login_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    login_time = Column(TIMESTAMP, default=datetime.utcnow)
    ip_address = Column(String(45))
