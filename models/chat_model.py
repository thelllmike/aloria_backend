from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class ChatConversation(Base):
    __tablename__ = "ChatConversations"
    conversation_id = Column(Integer, primary_key=True, index=True)
    user1_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    user2_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    messages = relationship("ChatMessage", back_populates="conversation")

class ChatMessage(Base):
    __tablename__ = "ChatMessages"
    message_id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('ChatConversations.conversation_id', ondelete='CASCADE'), nullable=False)
    sender_id = Column(Integer, ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    conversation = relationship("ChatConversation", back_populates="messages")
