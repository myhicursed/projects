from fastapi import FastAPI,HTTPException
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(creds: UserLoginSchema):
    if creds.username == "admin" and creds.password == "admin":
        token = security.create_access_token(uid="123")
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@app.get("/protected")
def protected():
    pass