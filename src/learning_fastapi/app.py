from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from learning_fastapi.database import get_session
from learning_fastapi.models import User

from learning_fastapi.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []

"""
@app.get("/Batatinha", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello World"}
"""

@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            User.username == user.username
            | User.email == user.email          
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Username already registered",
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Email already registered",
            )
        
        db_user = User(
            username = user.username,
            email = user.email,
            password = user.password,
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

"""
@app.get("/users/", status_code=HTTPStatus.OK, response_model=UserList)
def get_users():
    return {"user": database}


@app.put(
    "/users/{user_id}",
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete("/users/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    user_to_delete = UserDB(id=user_id, **database[user_id - 1].model_dump())
    database.remove(user_to_delete)
"""