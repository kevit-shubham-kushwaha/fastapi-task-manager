from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    

class UserResponse(User):
    _id:str
    username: str
    email: str
    password: str