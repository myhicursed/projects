from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Users(BaseModel):
    age: int
    name: str
    nickname: Optional[str]

@app.post("/users")
def create_user(age: int, name: str, nick: str, new_user: Users):
    new_user.age = age
    new_user.name = name
    if nick:
        new_user.nickname = nick
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run("t:app", reload = True)



for i in range(10):
    print(i)


n = int(input())
for i in range(n):
    print(i)
    for i in range(n):
        print(i)



