# models/suggestion_model.py

from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class SuggestionModel(Base):
    __tablename__ = "Suggestions"
    suggestion_id = Column(Integer, primary_key=True, index=True)
    skin_type_id = Column(Integer, ForeignKey('SkinTypes.skin_type_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('Products.product_id', ondelete='CASCADE'), nullable=False)
