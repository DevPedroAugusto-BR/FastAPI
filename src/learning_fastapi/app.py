from fastapi import FastAPI

app = FastAPI()

@app.get("/Batatinha")
def read_root():
    return {'message': 'Hello World'}
