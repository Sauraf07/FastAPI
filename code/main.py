from urllib.request import Request
#
# from fastapi import FastAPI
# app  = FastAPI
from fastapi import FastAPI

app = FastAPI()


# @app.post("/greet")
# def greet_user(name: "Khushi"):
#     return {"message": "Hello, " + name + "!"}
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/Khushi")
def read_root():
    return {"Hi Khushi"}
@app.get("/Saurav")
def read_root():
    return {"Saurav"}
# @app.post("/")
# def greet_user(name: str):
#     name = "Khushi"
#     return {"message": "Hello, " + name + "!"}