from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

app = FastAPI()

DATABASE_URL = "postgresql://postgres:myhicursed@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: str
    email: str
    is_active: bool = True

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.post("/users")
def create_user(usr: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=usr.username, email=usr.email, is_active=usr.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def len_lst(lst):
    return len(lst)