# Day 6: Response Models & Status Codes in FastAPI

> FastAPI Learning Roadmap - Day 6
>
> Goal: Learn how FastAPI sends responses, validates output data using Response Models, uses HTTP Status Codes, and builds professional APIs.

---

# Learning Objectives

By the end of this lesson, you will be able to:

✅ Understand API Responses

✅ Create Response Models

✅ Validate Response Data

✅ Use HTTP Status Codes

✅ Return Custom Responses

✅ Build Professional APIs

✅ Follow Backend Development Best Practices

---

# What is an API Response?

When a client sends a request to the server, the server sends back a response.

Example:

Client Request:

```http
GET /users/1
```

Server Response:

```json
{
    "id": 1,
    "name": "Saurav",
    "email": "saurav@gmail.com"
}
```

This returned data is called a Response.

---

# Request vs Response

| Request | Response |
|----------|-----------|
| Sent by Client | Sent by Server |
| Contains Input Data | Contains Output Data |
| POST /users | User Information |

Example:

```text
Client → Request → Server
Client ← Response ← Server
```

---

# Returning Data in FastAPI

Simple Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }
```

Response:

```json
{
    "message": "Welcome to FastAPI"
}
```

---

# What is a Response Model?

Response Model defines:

- What data should be returned
- Response structure
- Response validation
- Automatic API documentation

Think of it as a filter for outgoing data.

---

# Why Response Models?

Suppose your database contains:

```json
{
    "id": 1,
    "name": "Saurav",
    "email": "saurav@gmail.com",
    "password": "123456"
}
```

You never want to send passwords to users.

Response Models help hide sensitive data.

---

# Creating a Response Model

```python
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
```

---

# Using Response Model

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Saurav",
        "email": "saurav@gmail.com"
    }
```

---

# Response Model Filtering

Example:

```python
class UserResponse(BaseModel):
    id: int
    name: str

@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Saurav",
        "email": "secret@gmail.com"
    }
```

Response:

```json
{
    "id": 1,
    "name": "Saurav"
}
```

Notice:

```text
email is automatically removed
```

---

# Complete Request & Response Model Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):

    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
```

Response:

```json
{
    "id": 1,
    "name": "Saurav",
    "email": "saurav@gmail.com"
}
```

Password is removed automatically.

---

# What are HTTP Status Codes?

Status Codes tell the client what happened.

Examples:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error
```

---

# Common Status Codes

## 200 OK

Request successful.

```python
@app.get("/")
def home():
    return {"message": "Success"}
```

---

## 201 Created

Used when creating new resources.

Example:

```python
from fastapi import status

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user():
    return {"message": "User Created"}
```

Response Code:

```text
201 Created
```

---

## 400 Bad Request

Client sends invalid request.

Example:

```json
{
    "age": "abc"
}
```

---

## 401 Unauthorized

Authentication required.

Example:

```text
Token Missing
```

---

## 403 Forbidden

User authenticated but lacks permission.

Example:

```text
Admin Only Route
```

---

## 404 Not Found

Requested resource doesn't exist.

Example:

```text
User Not Found
```

---

## 500 Internal Server Error

Unexpected server error.

Example:

```python
1 / 0
```

---

# Using Status Module

Import:

```python
from fastapi import status
```

Examples:

```python
status.HTTP_200_OK

status.HTTP_201_CREATED

status.HTTP_404_NOT_FOUND

status.HTTP_500_INTERNAL_SERVER_ERROR
```

---

# Returning Custom Status Codes

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post(
    "/students",
    status_code=status.HTTP_201_CREATED
)
def create_student():
    return {
        "message": "Student Created"
    }
```

---

# Response Object

FastAPI allows direct control over responses.

```python
from fastapi import Response

@app.get("/")
def home(response: Response):

    response.status_code = 201

    return {
        "message": "Created"
    }
```

---

# Returning Custom Headers

```python
from fastapi import Response

@app.get("/")
def home(response: Response):

    response.headers["app-name"] = "FastAPI Learning"

    return {
        "message": "Success"
    }
```

---

# Response Description

Professional APIs include descriptions.

```python
@app.get(
    "/users",
    response_description="List of Users"
)
def get_users():
    return []
```

Swagger automatically displays this.

---

# Combining Everything

```python
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
```

---

# Mini Project

## Student Registration API

### Request Model

```python
name
email
age
course
```

### Response Model

```python
id
name
email
course
```

### Status Code

```python
201 Created
```

---

# Practice Tasks

## Task 1

Create Product API

Request:

```python
name
price
quantity
```

Response:

```python
id
name
price
```

---

## Task 2

Create Employee API

Request:

```python
name
department
salary
```

Response:

```python
employee_id
name
department
```

---

## Task 3

Create Course API

Request:

```python
course_name
duration
fees
```

Response:

```python
course_id
course_name
duration
```

---

## Task 4

Create Library API

Request:

```python
title
author
price
```

Response:

```python
book_id
title
author
```

---

# Interview Questions

## Beginner Level

### 1. What is a Response Model?

A Response Model defines the structure of data returned by an API.

---

### 2. Why use Response Models?

- Data Validation
- Security
- Documentation
- Cleaner APIs

---

### 3. What is response_model?

A FastAPI parameter used to define the response schema.

---

### 4. What is an HTTP Status Code?

A numeric code indicating the result of an API request.

---

### 5. What is 200 OK?

Request completed successfully.

---

## Intermediate Level

### 6. What is 201 Created?

Used when a new resource is successfully created.

---

### 7. What is 404 Not Found?

Requested resource doesn't exist.

---

### 8. Difference between Request Model and Response Model?

| Request Model | Response Model |
|--------------|----------------|
| Input Data | Output Data |
| Client → Server | Server → Client |

---

### 9. Can Response Models hide fields?

Yes.

Sensitive fields like passwords can be filtered automatically.

---

### 10. Why is response_model important?

It improves:

- Security
- Validation
- Documentation
- Maintainability

---

## Advanced Level

### 11. What happens if returned data doesn't match Response Model?

FastAPI raises a validation error.

---

### 12. Why should passwords never be returned?

Security reasons.

Passwords should always remain hidden.

---

### 13. What is the status module?

A FastAPI module containing HTTP status code constants.

---

### 14. What is response_description?

Adds API documentation details in Swagger UI.

---

### 15. What is the difference between 401 and 403?

| 401 | 403 |
|------|------|
| Not Authenticated | Not Authorized |
| Login Required | Permission Missing |

---

# Day 6 Summary

Today you learned:

✅ Response Models

✅ Response Validation

✅ Response Filtering

✅ HTTP Status Codes

✅ Status Module

✅ Custom Responses

✅ Response Headers

✅ Professional API Design

✅ Student Registration API

---

# Next Day (Day 7)

FastAPI CRUD Operations (Create, Read, Update, Delete) with In-Memory Database and Building a Complete Student Management API.