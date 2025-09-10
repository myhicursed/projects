from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/", tags=["Ручка"])
async def root():
    return {"message": "Hello"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

#docker run -p 1252:8000 my_image