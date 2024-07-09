from fastapi import FastAPI, APIRouter
from redis import Redis

from fastauth2 import FastAuth

app = FastAPI()
DB = Redis("redis", decode_responses=True)
AUTH = FastAuth()

app.include_router(AUTH.getRouter())


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
