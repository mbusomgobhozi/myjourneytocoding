from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


my_api = FastAPI()


@my_api.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@my_api.post("/upload")
def add_items():
    return


@my_api.delete("/")
def delete():
    return
