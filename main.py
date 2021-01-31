from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# TODO: Work on DB(Sqlite of MYSQL) in future
fakedb = []

# Craete a FastAPI app
app = FastAPI()

# Database Schema
class Item(BaseModel):
    id: int
    name: str
    is_done: bool

# Home page
@app.get("/")
def get_root():
    return {"welcome": "A welcome message"}

# Get all the todo Items
@app.get("/items")
def get_all_items():
    return fakedb

# Get one todo item based on its Id
@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = item_id-1
    return fakedb[item]

# Create a new todo Item
@app.post("/items")
def post_item(item: Item):
    fakedb.append(item.dict())
    return fakedb[-1]

# delete one todo item based on its Id
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = fakedb[item_id-1]
    fakedb.pop(item_id-1)
    return {"Item deleted successfully"}