from http import HTTPStatus
from fastapi import FastAPI

from learning_fastapi.schemas import Message

app = FastAPI()


@app.get("/Batatinha", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello World"}
