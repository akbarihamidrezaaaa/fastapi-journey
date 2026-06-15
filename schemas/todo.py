from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreateSchema(TodoBase):
    pass


class TodoUpdateSchema(BaseModel):
    id: int
    title: str
    description: str | None = None


class TodoReadSchema(BaseModel):
    id: int


class TodoDeleteSchema(BaseModel):
    id: int


class TodoResponseSchema(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
