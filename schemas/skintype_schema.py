# schemas/skintype_schema.py

from pydantic import BaseModel
from typing import Optional

class SkinTypeCreate(BaseModel):
    skin_type_name: str
    description: Optional[str] = None

class SkinTypeResponse(SkinTypeCreate):
    skin_type_id: int

    class Config:
        orm_mode: True
