from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float

app = FastAPI()

items = []

@app.get("/items/")
async def read_item():
    return items

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item
