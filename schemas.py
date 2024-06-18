from typing import Optional
from pydantic import BaseModel
from database import TaskOrm

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    
    
    
class STask(STaskAdd):
    id: int
    
    @classmethod
    def from_orm(cls, task_orm: TaskOrm):
        return cls(id=task_orm.id, name=task_orm.name, description=task_orm.description)
    
class STaskId(BaseModel):
    ok: bool = True
    task_id: int    