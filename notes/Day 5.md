# Day 5: Request Body & Pydantic Models in FastAPI

> FastAPI Learning Roadmap - Day 5
>
> Goal: Learn how to receive data from users using Request Body, validate data using Pydantic Models, and build real-world POST APIs.

---

# Learning Objectives

By the end of this lesson, you will be able to:

✅ Understand Request Body

✅ Create Pydantic Models

✅ Validate User Input

✅ Build POST APIs

✅ Handle JSON Data

✅ Understand Data Validation

✅ Create Real-World APIs

---

# What is Request Body?

When a client sends data to a server, the data is usually sent inside the Request Body.

Examples:

- User Registration
- Login
- Product Creation
- Blog Creation
- Student Registration

---

## Real World Example

Imagine a registration form:

```json
{
    "name": "Saurav",
    "email": "saurav@gmail.com",
    "age": 22
}
```

This data is sent from the frontend to the backend.

The backend receives it using a Request Body.

---

# What is JSON?

Most APIs communicate using JSON.

JSON = JavaScript Object Notation

Example:

```json
{
    "name": "Saurav",
    "age": 22,
    "city": "Indore"
}
```

JSON is lightweight and easy to read.

---

# FastAPI and Request Body

FastAPI automatically converts incoming JSON data into Python objects.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user(user: dict):
    return user
```

Request:

```json
{
    "name": "Saurav",
    "age": 22
}
```

Response:

```json
{
    "name": "Saurav",
    "age": 22
}
```

---

# Problem with Dictionary Approach

Using dictionaries has disadvantages:

❌ No Validation

❌ No Auto Documentation

❌ No Type Checking

❌ Difficult to Maintain

Example:

```json
{
    "name": 123,
    "age": "twenty"
}
```

FastAPI will accept invalid data.

---

# Solution: Pydantic

FastAPI uses Pydantic for data validation.

Pydantic validates incoming data automatically.

---

# What is Pydantic?

Pydantic is a Python library used for:

- Data Validation
- Data Parsing
- Type Checking
- Serialization

FastAPI heavily depends on Pydantic.

---

# Importing BaseModel

```python
from pydantic import BaseModel
```

Every request model inherits from BaseModel.

---

# Creating Your First Pydantic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Explanation:

```python
name: str
```

Means:

```text
name must be a string
```

```python
age: int
```

Means:

```text
age must be an integer
```

---

# Using Pydantic in FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

---

# Testing the API

Open:

```text
http://127.0.0.1:8000/docs
```

Try:

```json
{
    "name": "Saurav",
    "age": 22
}
```

Response:

```json
{
    "name": "Saurav",
    "age": 22
}
```

---

# Automatic Validation

Try:

```json
{
    "name": "Saurav",
    "age": "abc"
}
```

Response:

```json
{
    "detail": [
        {
            "type": "int_parsing",
            "msg": "Input should be a valid integer"
        }
    ]
}
```

FastAPI automatically validates data.

---

# Multiple Fields

Example:

```python
class User(BaseModel):
    name: str
    age: int
    email: str
    city: str
```

Request:

```json
{
    "name": "Saurav",
    "age": 22,
    "email": "saurav@gmail.com",
    "city": "Indore"
}
```

---

# Optional Fields

Sometimes fields are optional.

Example:

```python
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    city: Optional[str] = None
```

Valid Request:

```json
{
    "name": "Saurav",
    "age": 22
}
```

---

# Default Values

```python
class User(BaseModel):
    name: str
    age: int
    country: str = "India"
```

Request:

```json
{
    "name": "Saurav",
    "age": 22
}
```

Response:

```json
{
    "name": "Saurav",
    "age": 22,
    "country": "India"
}
```

---

# Nested Models

Real APIs often contain nested data.

Example:

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str

class User(BaseModel):
    name: str
    age: int
    address: Address
```

Request:

```json
{
    "name": "Saurav",
    "age": 22,
    "address": {
        "city": "Indore",
        "state": "MP"
    }
}
```

---

# List Data

Example:

```python
from typing import List

class User(BaseModel):
    name: str
    skills: List[str]
```

Request:

```json
{
    "name": "Saurav",
    "skills": [
        "Python",
        "FastAPI",
        "SQL"
    ]
}
```

---

# Complete Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "data": student
    }
```

---

# Understanding Data Flow

Client Sends:

```json
{
    "id": 1,
    "name": "Saurav",
    "age": 22,
    "course": "BCA"
}
```

↓

FastAPI Receives Request

↓

Pydantic Validates Data

↓

Python Object Created

↓

Function Executes

↓

Response Returned

---

# How FastAPI Converts Data

Incoming JSON:

```json
{
    "name": "Saurav",
    "age": 22
}
```

Converted Into:

```python
User(
    name="Saurav",
    age=22
)
```

You can access values:

```python
user.name
user.age
```

Example:

```python
@app.post("/users")
def create_user(user: User):
    return {
        "username": user.name
    }
```

---

# Using model_dump()

Pydantic V2:

```python
user.model_dump()
```

Example:

```python
@app.post("/users")
def create_user(user: User):
    return user.model_dump()
```

Output:

```json
{
    "name": "Saurav",
    "age": 22
}
```

---

# Mini Project

## Student Registration API

### Requirements

Fields:

```python
id
name
email
age
course
```

Endpoint:

```text
POST /students
```

Response:

```json
{
    "message": "Student Registered Successfully"
}
```

---

# Practice Tasks

## Task 1

Create User Model

Fields:

```python
name
email
age
```

---

## Task 2

Create Product Model

Fields:

```python
id
name
price
quantity
```

---

## Task 3

Create Book API

Fields:

```python
title
author
price
```

---

## Task 4

Create Employee API

Fields:

```python
id
name
department
salary
```

---

## Task 5

Create Course Registration API

Fields:

```python
student_name
course_name
duration
fees
```

---

# Interview Questions

## Beginner Level

### 1. What is Request Body?

A Request Body contains data sent by the client to the server.

---

### 2. What format is commonly used in APIs?

JSON.

---

### 3. What is Pydantic?

Pydantic is a Python library used for data validation and parsing.

---

### 4. Why does FastAPI use Pydantic?

For:

- Validation
- Type Checking
- Serialization
- Documentation

---

### 5. What is BaseModel?

BaseModel is the parent class used to create Pydantic models.

---

## Intermediate Level

### 6. Difference between Query Parameter and Request Body?

| Query Parameter | Request Body |
|---------------|--------------|
| URL Data | JSON Data |
| Mostly GET | Mostly POST |
| Small Data | Large Data |

---

### 7. How does FastAPI validate data?

Using Pydantic models.

---

### 8. What happens if validation fails?

FastAPI automatically returns a 422 Validation Error.

---

### 9. How do you make a field optional?

```python
Optional[str] = None
```

---

### 10. How do you provide default values?

```python
country: str = "India"
```

---

## Advanced Level

### 11. What are nested models?

Models inside another model.

---

### 12. What is model_dump()?

Converts a Pydantic model into a dictionary.

---

### 13. How does FastAPI generate documentation?

Using OpenAPI + Swagger UI automatically.

---

### 14. What is serialization?

Converting Python objects into JSON.

---

### 15. Why are Pydantic models preferred over dictionaries?

- Better Validation
- Better Readability
- Auto Documentation
- Type Safety
- Cleaner Code

---

# Day 5 Summary

Today you learned:

✅ Request Body

✅ JSON Basics

✅ Pydantic Models

✅ BaseModel

✅ Data Validation

✅ Optional Fields

✅ Default Values

✅ Nested Models

✅ Lists

✅ model_dump()

✅ Student Registration API

---

# Next Day (Day 6)

Response Models, Response Validation, Status Codes, and Building Professional APIs.