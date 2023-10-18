from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from main import combine
from pydantic import BaseModel
import json

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Item(BaseModel):
    input: str

class Output(BaseModel):
    output:list
    

foo = {}
@app.get("/")
def read_root():
    return {"Hello": "test"}

@app.get("/input")
def read_item():
    val = foo['value']
    finalOut = combine(val)
    return finalOut

@app.post("/output")
def post_item(item:Item):
    foo['value'] = item.input
    return item



