from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from core.database.database import SessionLocal, engine, Base
from core.database.crud import create_user, get_user_by_username
from core.auth.auth import hash_password, verify_password
from core.schemas.schema import UserCreate, UserLogin, UserResponse

app = FastAPI()
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Пользователь с таким логином уже существует")
    return create_user(db=db, user=user)




if __name__ == '__main__':
    uvicorn.run(app)