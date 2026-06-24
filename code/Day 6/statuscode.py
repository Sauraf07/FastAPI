# from fastapi import FastAPI, status

# app = FastAPI()

# @app.post(
#     "/students",
#     status_code=status.HTTP_201_CREATED
# )
# def create_student():
#     return {
#         "message": "Student Created"
#     }

# from fastapi import Response

# # @app.get("/")
# # def home(response: Response):

# #     response.status_code = 201

# #     return {
# #         "message": "Created"
# #     }

# from fastapi import Response

# @app.get("/")
# def home(response: Response):

#     response.headers["app-name"] = "FastAPI Learning"

#     return {
#         "message": "Success"
#     }

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    age: int
    course: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):

    return {
        "id": 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }