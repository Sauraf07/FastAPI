from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return{"This is my mini project"}

@app.get("/Home")
def read_home():
    return{"This is my home page"}

@app.get("/About")
def read_about():
    return{"This is my about page"}

@app.get("/Contact")
def read_contact():
    return{"This is my contact page"}