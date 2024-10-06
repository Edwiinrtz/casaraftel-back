from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

URI = os.getenv('RAFTEL_BDA_URI')
client = MongoClient(URI)
database  = client["raftel"]
colletion = database["content"]
app = FastAPI()
origins = [
    "https://casaraftel.com/",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/content', response_model=list())
def content():
    lista = [{'type': i["type"],'url': i["url"],'date': i["date"]} for i in colletion.find()]
    return lista
