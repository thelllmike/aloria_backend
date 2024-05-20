# schemas/login_history_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LoginHistoryCreate(BaseModel):
    user_id: int
    ip_address: Optional[str] = None

class LoginHistoryResponse(LoginHistoryCreate):
    login_id: int
    login_time: datetime

    class Config:
        orm_mode: True
