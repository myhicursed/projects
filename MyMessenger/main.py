from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from core.database.database import SessionLocal, engine, Base
from core.database.crud import create_user, get_user_by_username
from core.auth.auth import hash_password, verify_password
from core.schemas.schema import UserCreate, UserLogin, UserResponse, MessageCreate, MessageResponse
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
    return db_msg

@app.get("/messages", response_model=List[MessageResponse])
def get_messages(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(
        ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
        ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
    ).order_by(Message.timestamp).all()

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


#if __name__ == '__main__':
#    uvicorn.run(app, port=8000)