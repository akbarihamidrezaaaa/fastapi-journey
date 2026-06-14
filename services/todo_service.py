from sqlalchemy.orm import Session

from models.todo import TodoModel


def create_todo(db, request):
    new_todo = TodoModel(title=request.title, description=request.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todos(db):
    all_todos = db.query(TodoModel).all()
    return all_todos


def get_specefic_todo(db, id):
    db_todo = db.query(TodoModel).filter_by(id=id).one_or_none()
    return db_todo


def update_todo(db: Session, request):
    db_todo = db.query(TodoModel).filter_by(id=request.id).one_or_none()
    db_todo.title = request.title
    db_todo.description = request.description
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db, todo_id):
    db_todo = db.query(TodoModel).filter_by(id=todo_id).one_or_none()
    db.delete(db_todo)
    db.commit()
