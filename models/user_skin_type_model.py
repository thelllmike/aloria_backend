# models/user_skin_type_model.py

from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from database import Base

class UserSkinTypeModel(Base):
    __tablename__ = "UserSkinTypes"
    user_skin_type_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    skin_type_id = Column(Integer, ForeignKey('SkinTypes.skin_type_id', ondelete='CASCADE'), nullable=False)
    detected_at = Column(TIMESTAMP, default=datetime.utcnow)
