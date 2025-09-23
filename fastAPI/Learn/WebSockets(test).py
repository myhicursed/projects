from fastapi import FastAPI
from starlette.websockets import WebSocket
import logging
import uvicorn

logger = logging.Logger(__name__)


app = FastAPI()

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        logger.info(data)
        await websocket.send_text(data)

uvicorn.run(app)
