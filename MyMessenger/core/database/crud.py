from sqlalchemy.orm import Session
from ..schemas.schema import UserCreate, UserLogin, UserResponse
from ..auth.auth import hash_password, verify_password
from .models import User

def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(login=user.login, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.login == username).first()