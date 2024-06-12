from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ChatMessageCreate(BaseModel):
    conversation_id: int
    sender_id: int
    message: str

class ChatMessageResponse(ChatMessageCreate):
    message_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChatConversationCreate(BaseModel):
    user1_id: int
    user2_id: int

class ChatConversationResponse(ChatConversationCreate):
    conversation_id: int
    created_at: datetime
    messages: List[ChatMessageResponse] = []

    class Config:
        from_attributes = True
