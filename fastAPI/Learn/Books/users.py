from fastapi import APIRouter

api_router = APIRouter(prefix="/users")

@api_router.get("/")
def get_users():
    return {"message": "Вывод пользователей"}