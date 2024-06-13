# schemas/login_schema.py

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    user_id: int  # Add user_id to the response schema


class TokenData(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str
