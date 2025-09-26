from fastapi import FastAPI, Response, Cookie
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import uvicorn

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0, lt=90)
    email: str

    @field_validator('email')
    def validate_email(cls, email):
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email

@app.get("/reg")
def root(response: Response):
    now = datetime.now()
    response.set_cookie("last_visit", value=now)
    return {"message": "куки установлены"}
@app.get("/cookies")
def cookie(last_visit = Cookie()):
    return {"cookie": last_visit}

uvicorn.run(app)
