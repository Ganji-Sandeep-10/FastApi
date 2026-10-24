from pydantic import BaseModel,Field,ConfigDict,model_validator
from datetime import datetime

class Task(BaseModel):
    title:str=Field(min_length=1,max_length=100)
    description:str=Field(min_length=1,max_length=500)
    completed:bool=Field(default=False)

class TaskCreate(Task):
    pass

class TaskResponse(Task):
    model_config=ConfigDict(from_attributes=True)
    id:int
    created_at:datetime


class TaskUpdate(BaseModel):
    title:str|None=Field(default=None,min_length=1,max_length=100)
    description:str|None=Field(default=None,min_length=1,max_length=500)
    completed:bool|None=None

    @model_validator(mode="after")
    def check_not_empty(self):
        if not self.model_fields_set:
            raise ValueError("Send at least one field to update")
        return self
