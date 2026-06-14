from fastapi import FastAPI

from core.database import Base, engine
from routers.todos import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router)
