from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/Saurav")
def read_saurav():
    return {"name": "Saurav", "age": 22, "city": "Bangalore"}

@app.get("/Friends")
def read_friends():
    return {"Khushi ":"Saurav"}