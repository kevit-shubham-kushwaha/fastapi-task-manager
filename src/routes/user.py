from fastapi import APIRouter, Depends
from utils.libs.schemas.users import User as UserSchema
from utils.libs.db.repository import user_collection_instance

routes = APIRouter(

    prefix="/users",
    tags=["user"],
)


class UserRoute:
  
  @staticmethod
  @routes.get("/")
  async def read_user():
   try:
     users_data = user_collection_instance.find_many({})
     if not users_data:
       return {
          "message":"No users found",
          "status":404
       }
       
     users = []
     for user in users_data:
        user["_id"] = str(user["_id"])
        users.append(user)
      
      
        
        
     print(users)
    #  return_data = UserSchema(**user_dict)
        
     return {
        "message":"Users fetch Successfully",
        "status":200,
        "data":users
     }  
       
     
   except Exception as e:
     return {
        "message":"Internal Server Error",
        "status":500,
        "error":str(e)  
     }

  
  
  
  
  
  
  
