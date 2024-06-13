# models.models
import enum 
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP ,Enum
from database import Base
from datetime import datetime

class UserRole(enum.Enum):
    customer = "customer"
    admin = "admin"

class UserModel(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    role = Column(Enum(UserRole), default=UserRole.customer, nullable=False)


class Address(Base):
    __tablename__ = "Addresses"
    address_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    address_line1 = Column(String(255), nullable=False)
    address_line2 = Column(String(255))
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
