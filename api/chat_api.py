# api/chat_api.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud.chat_crud as crud
import schemas.chat_schemas as schemas
from database import get_db

router = APIRouter()

@router.post("/conversations/", response_model=schemas.ChatConversationResponse)
def create_conversation(conversation: schemas.ChatConversationCreate, db: Session = Depends(get_db)):
    db_conversation = crud.create_conversation(db, conversation)
    return db_conversation

@router.get("/conversations/{conversation_id}", response_model=schemas.ChatConversationResponse)
def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    db_conversation = crud.get_conversation(db, conversation_id)
    if db_conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return db_conversation

@router.post("/messages/", response_model=schemas.ChatMessage)
def create_message(message: schemas.ChatMessageCreate, db: Session = Depends(get_db)):
    db_message = crud.create_message(db, message)
    return db_message


@router.get("/conversations/", response_model=List[schemas.ChatConversationResponse])
def get_conversations(db: Session = Depends(get_db)):
    db_conversations = crud.get_conversations(db)
    return db_conversations

@router.get("/conversations/{conversation_id}", response_model=List[schemas.ChatMessage])
def get_conversation_messages(conversation_id: int, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, conversation_id)
    if messages is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return messages




@router.delete("/messages/{message_id}", response_class=JSONResponse)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    success = crud.delete_message(db, message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"detail": "Message deleted"}

@router.delete("/conversations/{conversation_id}", response_class=JSONResponse)
def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    success = crud.delete_conversation(db, conversation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return {"detail": "Conversation deleted"}
