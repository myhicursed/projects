from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class UserCreate(BaseModel):
    login: str
    password: str


class UserLogin(BaseModel):
    login: str
    password: str


class UserResponse(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    sender_id: int
    receiver_id: Optional[int] = None
    chat_id: Optional[int] = None
    text: str


class MessageResponse(BaseModel):
    id: int
    sender: str  # логин отправителя
    receiver_id: Optional[int]
    chat_id: Optional[int]
    text: str
    timestamp: datetime

    class Config:
        from_attributes = True



class ChatCreate(BaseModel):
    name: Optional[str]
    members: List[str]      # логины участников


class ChatResponse(BaseModel):
    id: int
    name: Optional[str]
    created_by: Optional[str]   # логин создателя
    created_at: datetime

    class Config:
        from_attributes = True


class ChatListItem(BaseModel):
    id: int
    name: Optional[str]

    class Config:
        from_attributes = True
