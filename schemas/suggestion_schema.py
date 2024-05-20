# schemas/suggestion_schema.py

from pydantic import BaseModel

class SuggestionCreate(BaseModel):
    skin_type_id: int
    product_id: int

class SuggestionResponse(SuggestionCreate):
    suggestion_id: int

    class Config:
        orm_mode: True
