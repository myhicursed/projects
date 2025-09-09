from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import uvicorn
app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": None,
    "age": 12,
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    age: int = Field(ge=0, le=100)
users = []
@app.post("/users", tags=["Добавление пользователей"])
def add_user(user: UserSchema):
    users.append(user)
    return {"success": 200, "msg": "Пользователь добавлен"}
@app.get("/users", tags=["Получение пользователей"])
def get_users():
    return users


if __name__ == "__main__":
    uvicorn.run("main1:app", reload = True)