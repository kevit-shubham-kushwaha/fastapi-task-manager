from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    status: str
    
    
class TaskResponse(Task):
    _id: str
    title: str
    description: str
    status: str
    