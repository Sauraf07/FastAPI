from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/student")
def student():
    return {
        "name": "Saurav",
        "course": "BCA"
    }

@app.get("/skills")
def skills():
    return [
        "Python",
        "FastAPI",
        "SQL"
    ]