import time
import asyncio
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def sync_task():
    time.sleep(3)
    print("Отправлен email")
async def async_task():
    await asyncio.sleep(3)
    print("Сделан запрос в сторонний API")

@app.post("/")
async def some_route():
    asyncio.create_task(async_task())
    return {"ok": True}

@app.post("/d")
async def another_route(bg_task: BackgroundTasks):
    bg_task.add_task(sync_task)
    return {"ok": True}