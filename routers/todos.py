from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.todo import (
    TodoCreateSchema,
    TodoResponseSchema,
    TodoUpdateSchema,
)
from services.todo_service import (
    create_todo,
    delete_todo,
    get_all_todos,
    get_specefic_todo,
    update_todo,
)

router = APIRouter()


@router.post("/todo/create", response_model=TodoResponseSchema)
async def create_todos(request: TodoCreateSchema, db: Session = Depends(get_db)):
    new_todo = create_todo(db, request)
    return new_todo


@router.get("/todo/readall", response_model=list[TodoResponseSchema])
async def read_all_todos(db: Session = Depends(get_db)):
    return get_all_todos(db)


@router.get("/todo/read", response_model=TodoResponseSchema)
async def read_specefic_todo(id: int, db: Session = Depends(get_db)):
    return get_specefic_todo(db, id)


@router.post("/todo/update", response_model=TodoResponseSchema)
async def update_todos(request: TodoUpdateSchema, db: Session = Depends(get_db)):
    return update_todo(db, request)


@router.delete("/todo/delete", response_model=TodoResponseSchema)
async def delete_todos(todo_id: int, db: Session = Depends(get_db)):
    delete_todo(db, todo_id)
    return JSONResponse(content=f"todo with id: {todo_id} deleted successfully.")
