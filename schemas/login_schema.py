# schemas/login_schema.py

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str


class TokenData(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str
