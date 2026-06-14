from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreateSchema(TodoBase):
    pass


class TodoUpdateSchema(TodoBase):
    id: int


class TodoReadSchema(BaseModel):
    id: int


class TodoDeleteSchema(BaseModel):
    id: int


class TodoResponseSchema(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
