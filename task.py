from pydantic import BaseModel, Field 

class Task(BaseModel): 
    id : str = Field(..., description="The unique identifier for the task.") 
    name: str = Field(..., description="The name of the task.") 
    is_completed: bool = Field(False, description="Indicates whether the task is completed or not.")