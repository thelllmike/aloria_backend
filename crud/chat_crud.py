from sqlalchemy.orm import Session
import models.chat_model as models
import schemas.chat_schemas as schemas

def create_conversation(db: Session, conversation: schemas.ChatConversationCreate):
    db_conversation = models.ChatConversation(**conversation.dict())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def get_conversation(db: Session, conversation_id: int):
    return db.query(models.ChatConversation).filter(models.ChatConversation.conversation_id == conversation_id).first()

def create_message(db: Session, message: schemas.ChatMessageCreate):
    db_message = models.ChatMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, conversation_id: int):
    return db.query(models.ChatMessage).filter(models.ChatMessage.conversation_id == conversation_id).all()
