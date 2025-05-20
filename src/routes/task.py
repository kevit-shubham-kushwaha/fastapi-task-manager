from fastapi import APIRouter, Depends, Query, HTTPException
from utils.libs.schemas.tasks import Task as TaskSchema , TaskResponse

from utils.libs.db.repository import task_collection_instance

routes = APIRouter(

    prefix="/tasks",
    tags=["tasks"],
)

class TaskRoute:
  
  @staticmethod
  @routes.get("/")
  async def read_task():
   try:
     task_data = task_collection_instance.find_many({})
     if not task_data:
       return {
          "message":"No users found",
          "status":404
       }
       
     tasks = []
     for task in task_data:
        task["_id"] = str(task["_id"])
        tasks.append(task)
       
     return {
        "message":"Task fetch Successfully",
        "status":200,
        "data":tasks
     }  
       
     
   except Exception as e:
     return {
        "message":"Internal Server Error",
        "status":500,
        "error":str(e)  
     }

  @staticmethod
  @routes.post("/")
  def create_task(task: TaskSchema):
      try:
          task_dict = task.dict()
          result = task_collection_instance.insert_one(task_dict)
          task_dict["_id"] = str(result.inserted_id)

          
          return {
              "message": "Task Created Successfully",
              "status": 200,
              "data": task_dict
          }
      except Exception as e:
          return {
              "message": "Internal Server Error",
              "status": 500,
              "error": str(e)
          }
          
          
  @staticmethod
  @routes.get("/{task_id}")
  def update_task(task_id:str,task_data:TaskSchema):
      try:
          task_dict = task_data.dict()
          result = task_collection_instance.update_one({"_id": task_id}, {"$set": task_dict})
          if result.modified_count == 0:
              return {
                  "message": "Task not found",
                  "status": 404
              }
          task_dict["_id"] = str(task_id)
          return {
              "message": "Task Updated Successfully",
              "status": 200,
              "data": task_dict
          }
      except Exception as e:
          return {
              "message": "Internal Server Error",
              "status": 500,
              "error": str(e)
          }
  
  @staticmethod
  @routes.delete("/{task_id}")
  def delete_task(task_id:str):
      try:
          result = task_collection_instance.delete_one({"_id": task_id})
          if result.deleted_count == 0:
              return {
                  "message": "Task not found",
                  "status": 404
              }
          return {
              "message": "Task Deleted Successfully",
              "status": 200
          }
      except Exception as e:
          return {
              "message": "Internal Server Error",
              "status": 500,
              "error": str(e)
          }