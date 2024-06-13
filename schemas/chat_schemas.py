from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ChatMessage(BaseModel):
    message_id: int
    conversation_id: int
    sender_id: int
    sender_username: str  # Added this field
    message: str
    created_at: datetime

    class Config:
        orm_mode = True

class ChatConversationBase(BaseModel):
    user1_id: int
    user2_id: int

class ChatConversationCreate(ChatConversationBase):
    pass

class ChatConversation(ChatConversationBase):
    conversation_id: int
    created_at: datetime
    user1_username: Optional[str]
    user2_username: Optional[str]
    messages: List[ChatMessage]

    class Config:
        orm_mode = True

class ChatConversationResponse(BaseModel):
    conversation_id: int
    user1_id: int
    user2_id: int
    user1_username: str
    user2_username: str
    created_at: datetime
    messages: List[ChatMessage] = []

    class Config:
        orm_mode = True

class ChatMessageCreate(BaseModel):
    conversation_id: int
    sender_id: int
    message: str
