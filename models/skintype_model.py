# models/skintype_model.py

from sqlalchemy import Column, Integer, String, Text
from database import Base

class SkinTypeModel(Base):
    __tablename__ = "SkinTypes"
    skin_type_id = Column(Integer, primary_key=True, index=True)
    skin_type_name = Column(String(50), nullable=False)
    description = Column(Text)
