from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
