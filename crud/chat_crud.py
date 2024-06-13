# crud/chat_crud.py

from sqlalchemy.orm import Session
import models.chat_model as models
import schemas.chat_schemas as schemas
import models.models as User

def create_conversation(db: Session, conversation: schemas.ChatConversationCreate):
    db_conversation = models.ChatConversation(**conversation.dict())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)

    user1 = db.query(User.UserModel).filter(User.UserModel.user_id == db_conversation.user1_id).first()
    user2 = db.query(User.UserModel).filter(User.UserModel.user_id == db_conversation.user2_id).first()

    return {
        "conversation_id": db_conversation.conversation_id,
        "user1_id": db_conversation.user1_id,
        "user2_id": db_conversation.user2_id,
        "user1_username": user1.username if user1 else None,
        "user2_username": user2.username if user2 else None,
        "created_at": db_conversation.created_at,
        "messages": []
    }

def get_conversation(db: Session, conversation_id: int):
    conversation = db.query(models.ChatConversation).filter(models.ChatConversation.conversation_id == conversation_id).first()
    if not conversation:
        return None
    user1 = db.query(User.UserModel).filter(User.UserModel.user_id == conversation.user1_id).first()
    user2 = db.query(User.UserModel).filter(User.UserModel.user_id == conversation.user2_id).first()
    messages_with_usernames = []
    for msg in conversation.messages:
        sender = db.query(User.UserModel).filter(User.UserModel.user_id == msg.sender_id).first()
        messages_with_usernames.append({
            "message_id": msg.message_id,
            "conversation_id": msg.conversation_id,
            "sender_id": msg.sender_id,
            "sender_username": sender.username if sender else None,
            "message": msg.message,
            "created_at": msg.created_at
        })
    return {
        "conversation_id": conversation.conversation_id,
        "user1_id": conversation.user1_id,
        "user2_id": conversation.user2_id,
        "user1_username": user1.username if user1 else None,
        "user2_username": user2.username if user2 else None,
        "created_at": conversation.created_at,
        "messages": messages_with_usernames
    }

def create_message(db: Session, message: schemas.ChatMessageCreate):
    db_message = models.ChatMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    
    sender = db.query(User.UserModel).filter(User.UserModel.user_id == db_message.sender_id).first()
    
    return {
        "message_id": db_message.message_id,
        "conversation_id": db_message.conversation_id,
        "sender_id": db_message.sender_id,
        "sender_username": sender.username if sender else None,
        "message": db_message.message,
        "created_at": db_message.created_at
    }


def get_messages(db: Session, conversation_id: int):
    return db.query(models.ChatMessage).filter(models.ChatMessage.conversation_id == conversation_id).all()

def get_conversations(db: Session):
    conversations = db.query(models.ChatConversation).all()
    conversation_list = []
    for conversation in conversations:
        user1 = db.query(User.UserModel).filter(User.UserModel.user_id == conversation.user1_id).first()
        user2 = db.query(User.UserModel).filter(User.UserModel.user_id == conversation.user2_id).first()
        messages_with_usernames = []
        for msg in conversation.messages:
            sender = db.query(User.UserModel).filter(User.UserModel.user_id == msg.sender_id).first()
            receiver_username = user2.username if msg.sender_id == conversation.user1_id else user1.username
            messages_with_usernames.append({
                "message_id": msg.message_id,
                "conversation_id": msg.conversation_id,
                "sender_id": msg.sender_id,
                "sender_username": sender.username if sender else None,
                "receiver_username": receiver_username,
                "message": msg.message,
                "created_at": msg.created_at
            })
        conversation_list.append({
            "conversation_id": conversation.conversation_id,
            "user1_id": conversation.user1_id,
            "user2_id": conversation.user2_id,
            "user1_username": user1.username if user1 else None,
            "user2_username": user2.username if user2 else None,
            "created_at": conversation.created_at,
            "messages": messages_with_usernames
        })
    return conversation_list


def delete_message(db: Session, message_id: int):
    message = db.query(models.ChatMessage).filter(models.ChatMessage.message_id == message_id).first()
    if message:
        db.delete(message)
        db.commit()
        return True
    return False

def delete_conversation(db: Session, conversation_id: int):
    conversation = db.query(models.ChatConversation).filter(models.ChatConversation.conversation_id == conversation_id).first()
    if conversation:
        db.delete(conversation)
        db.commit()
        return True
    return False
