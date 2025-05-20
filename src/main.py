from fastapi import FastAPI
import uvicorn
from utils.libs.config import (PORT,HOST)
from src.routes.user import routes as user_routes

app = FastAPI()

app.include_router(user_routes)

@app.get("/")
def read_root():
    return {"Hello": "World"}
  

if __name__ == "__main__":
    uvicorn.run("app:app", host=HOST, port=PORT, reload=False)