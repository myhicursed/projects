from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from core.database.database import SessionLocal, engine, Base
from core.database.crud import create_user, get_user_by_username, create_chat, get_user_chats, add_user_to_chat, get_chat_messages, send_chat_message
from core.auth.auth import hash_password, verify_password
from core.schemas.schema import UserCreate, UserLogin, UserResponse, MessageCreate, MessageResponse, ChatCreate, ChatResponse, ChatListItem
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from core.database.models import User, Message
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
@app.get("/")
def root():
    return FileResponse("templates/registerForm.html")
@app.get("/main")
def main_page():
    return FileResponse("templates/index.html")

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/messages", response_model=MessageResponse)
def send_message(msg: MessageCreate, db: Session = Depends(get_db)):
    db_msg = Message(**msg.dict())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)

    sender = db.query(User).filter(User.id == db_msg.sender_id).first()
    return {
        "id": db_msg.id,
        "sender": sender.login if sender else None,
        "receiver_id": db_msg.receiver_id,
        "chat_id": db_msg.chat_id,
        "text": db_msg.text,
        "timestamp": db_msg.timestamp
    }

@app.get("/messages", response_model=List[MessageResponse])
def get_messages(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(
        ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
        ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
    ).order_by(Message.timestamp).all()

    result = []
    for msg in messages:
        sender = db.query(User).filter(User.id == msg.sender_id).first()
        result.append({
            "id": msg.id,
            "sender": sender.login if sender else None,
            "receiver_id": msg.receiver_id,
            "chat_id": msg.chat_id,
            "text": msg.text,
            "timestamp": msg.timestamp
        })
    return result


@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.login)
    if db_user:
        raise HTTPException(status_code=401, detail="Пользователь с таким логином уже существует")
    return create_user(db=db, user=user)

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.login)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    return {"message": "Успешно", "user_id": db_user.id}

@app.post("/chats/create", response_model=ChatResponse)
def api_create_chat(payload: ChatCreate, db: Session = Depends(get_db)):
    try:
        chat = create_chat(
            db,
            name=payload.name,
            member_logins=payload.members,
            creator_login=payload.members[0]
        )

        creator = db.query(User).filter(User.id == chat.created_by).first()
        return {
            "id": chat.id,
            "name": chat.name,
            "created_by": creator.login if creator else None,
            "created_at": chat.created_at  # добавляем!
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Получить чаты пользователя
@app.get("/users/{user_id}/chats", response_model=List[ChatListItem])
def api_get_user_chats(user_id: int, db: Session = Depends(get_db)):
    chats = get_user_chats(db, user_id)
    return chats

# Получить сообщения чата
@app.get("/chats/{chat_id}/messages", response_model=List[MessageResponse])
def api_get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    messages = get_chat_messages(db, chat_id)
    # get_chat_messages уже возвращает словари с 'sender': sender.login
    return messages

# Отправить сообщение в чат
@app.post("/chats/{chat_id}/messages", response_model=MessageResponse)
def api_send_chat_message(chat_id: int, payload: MessageCreate, db: Session = Depends(get_db)):
    msg = send_chat_message(db, chat_id=chat_id if chat_id else None, sender_id=payload.sender_id, text=payload.text)

    sender = db.query(User).filter(User.id == payload.sender_id).first()

    return {
        "id": msg.id,
        "chat_id": msg.chat_id,
        "sender": sender.login if sender else None,
        "receiver_id": msg.receiver_id,
        "text": msg.text,
        "timestamp": msg.timestamp
    }

#if __name__ == '__main__':
#    uvicorn.run(app, port=8000)