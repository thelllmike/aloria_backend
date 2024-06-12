from typing import List
from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/messages/", response_model=schemas.ChatMessageResponse)
def create_message(message: schemas.ChatMessageCreate, db: Session = Depends(get_db)):
    db_message = crud.create_message(db, message)
    return db_message

@router.get("/conversations/{conversation_id}/messages", response_model=List[schemas.ChatMessageResponse])
def get_messages(conversation_id: int, db: Session = Depends(get_db)):
    return crud.get_messages(db, conversation_id)
