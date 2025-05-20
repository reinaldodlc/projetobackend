from fastapi import FastAPI

app = FastAPI()

items = [{"item_name": "Arroz"}, {"item_name": "Feijão"}, {"item_name": "Macarrão"}]

@app.get("/items/")
async def read_item():
    return items