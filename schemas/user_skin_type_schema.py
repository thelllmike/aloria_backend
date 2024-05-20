# schemas/user_skin_type_schema.py

from pydantic import BaseModel
from datetime import datetime

class UserSkinTypeCreate(BaseModel):
    user_id: int
    skin_type_id: int

class UserSkinTypeResponse(UserSkinTypeCreate):
    user_skin_type_id: int
    detected_at: datetime

    class Config:
        orm_mode: True
