from pydantic import BaseModel
from datetime import datetime
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
    receiver_id: int
    text: str

class MessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    text: str
    timestamp: datetime
    class Config:
        from_attributes = True
