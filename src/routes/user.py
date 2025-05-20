from fastapi import APIRouter, Depends
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

routes = APIRouter(

    prefix="/users",
    tags=["user"],
)

fake_users_db = {
    "Bob": {"username": "Bob", "email": "Bob@email.com", "password": "Bob123"}
}

class UserRoute:
  
  @staticmethod
  @routes.get("/", response_model=User)
  async def read_user():
    user_data = fake_users_db.get("Bob")
    user = User(**user_data.copy())
    return user
  
  
  
  
  
  
