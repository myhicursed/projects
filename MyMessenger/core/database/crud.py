from sqlalchemy.orm import Session
from ..schemas.schema import UserCreate, UserLogin, UserResponse
from ..auth.auth import hash_password, verify_password
from .models import User, Chat, ChatMember, Message

def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(login=user.login, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.login == username).first()

def create_chat(db: Session, name: str, member_logins: list, creator_login: str):
    creator = get_user_by_username(db, creator_login)
    if not creator:
        raise ValueError("Creator doesn't exist")
    chat = Chat(name=name, created_by=creator.id)
    db.add(chat)
    db.flush()

    members = set(member_logins)
    members.add(creator_login)

    for login in members:
        user = get_user_by_username(db, login)
        if user:
            cm = ChatMember(chat_id=chat.id, user_id=user.id)
            db.add(cm)

    db.commit()
    db.refresh(chat)
    return chat

def get_user_chats(db: Session, user_id: int):
    # возвращаем чаты, в которых состоит пользователь
    rows = db.query(Chat).join(ChatMember, Chat.id == ChatMember.chat_id).filter(ChatMember.user_id == user_id).all()
    return rows

def add_user_to_chat(db: Session, chat_id: int, user_login: str):
    user = get_user_by_username(db, user_login)
    if not user:
        return None
    exists = db.query(ChatMember).filter(ChatMember.chat_id==chat_id, ChatMember.user_id==user.id).first()
    if exists:
        return exists
    cm = ChatMember(chat_id=chat_id, user_id=user.id)
    db.add(cm)
    db.commit()
    db.refresh(cm)
    return cm

def get_chat_messages(db: Session, chat_id: int):
    messages = db.query(Message).filter(Message.chat_id == chat_id).all()
    result = []
    for msg in messages:
        sender = db.query(User).filter(User.id == msg.sender_id).first()
        result.append({
            "id": msg.id,
            "chat_id": msg.chat_id,
            "sender": sender.login if sender else None,
            "receiver_id": msg.receiver_id,  # добавляем!
            "text": msg.text,
            "timestamp": msg.timestamp
        })
    return result


def send_chat_message(db: Session, chat_id: int, sender_id: int, text: str):
    msg = Message(chat_id=chat_id, sender_id=sender_id, text=text)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg