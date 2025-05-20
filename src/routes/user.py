from fastapi import APIRouter, Depends, Query, HTTPException
from utils.libs.schemas.users import User as UserSchema , UserResponse
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

  @staticmethod
  @routes.post("/")
  def create_user(user: UserSchema):
      try:
          user_dict = user.dict()
          result = user_collection_instance.insert_one(user_dict)
          user_dict["_id"] = str(result.inserted_id)

          
          return {
              "message": "User Created Successfully",
              "status": 200,
              "data": user_dict
          }

      except Exception as e:
          raise HTTPException(status_code=500, detail={
              "message": "Internal Server Error",
              "error": str(e)
          })
    
  @staticmethod
  @routes.put("/{user_id}")
  def update_user(user_id:str,user_data:UserSchema):
    try:
      user_dict = user_data.model_dump(exclude_none=True)
      user_dict["_id"] = user_id
      
      updated_user = user_collection_instance.insert_one(user_dict)
      
      
      if not updated_user:
        return {
          "message":"User Update Failed",
          "status":500
        }
      
      return {
        "message":"User Updated Successfully",
        "status":200,
        "data":user_dict
      }
      
    except Exception as e:
      
      raise {
        "message":"Internal Server Error",
        "status":500,
        "error":str(e)  
      }
  
  @staticmethod
  @routes.delete("/{user_id}",response_model=UserSchema)
  def delete_user(user:UserSchema):
    try:
      user_dict = user.dict()
      user_dict["_id"] = str(user_dict["_id"])
      
      deleted_user = user_collection_instance.delete_one({"_id":user_dict["_id"]})
      
      if not deleted_user:
        return {
          "message":"User Deletion Failed",
          "status":500
        }
      
      return {
        "message":"User Deleted Successfully",
        "status":200,
        "data":user_dict
      }
      
    except Exception as e:
      
      raise {
        "message":"Internal Server Error",
        "status":500,
        "error":str(e)  
      }
  
  
  
  
  
