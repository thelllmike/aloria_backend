# models/chat_model.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class ChatConversation(Base):
    __tablename__ = "chat_conversations"
    conversation_id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey('Users.user_id'))
    user2_id = Column(Integer, ForeignKey('Users.user_id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    messages = relationship("ChatMessage", back_populates="conversation")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    message_id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('chat_conversations.conversation_id'))
    sender_id = Column(Integer, ForeignKey('Users.user_id'))
    message = Column(String(500), index=True)  # Specify the length of the String
    created_at = Column(DateTime, default=datetime.utcnow)
    conversation = relationship("ChatConversation", back_populates="messages")
