# Day 2 - FastAPI Setup & Your First API 🚀

## Goal of Day 2

By the end of today, you will:

- Understand what FastAPI is
- Install FastAPI and Uvicorn
- Create your first FastAPI application
- Run a local development server
- Understand API routes
- Learn route decorators
- Explore automatic API documentation
- Build multiple API endpoints
- Understand request-response flow
- Be ready for Day 3 (Path Parameters)

---

# What is FastAPI?

FastAPI is a modern Python web framework used to build APIs quickly and efficiently.

It is:

- Fast
- Easy to learn
- Built on Python Type Hints
- Automatically generates API documentation
- Supports async programming
- Used in production by many companies

### Why FastAPI?

Compared to Flask and Django:

| Feature | FastAPI | Flask | Django |
|----------|----------|----------|----------|
| Speed | Very Fast | Medium | Medium |
| Auto Documentation | ✅ | ❌ | ❌ |
| Type Validation | ✅ | ❌ | Limited |
| Async Support | ✅ | Limited | Limited |
| Easy to Learn | ✅ | ✅ | Medium |

---

# How APIs Work

```
Client
   ↓
HTTP Request
   ↓
FastAPI Server
   ↓
Business Logic
   ↓
Database (Optional)
   ↓
Response
   ↓
Client
```

Example:

```
Browser
   ↓
GET /hello
   ↓
FastAPI
   ↓
Returns JSON
```

Response:

```json
{
  "message": "Hello World"
}
```

---

# Install Python

Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

Expected:

```bash
Python 3.10+
```

---

# Create Project Folder

```bash
mkdir fastapi-learning
cd fastapi-learning
```

---

# Create Virtual Environment

Why?

Virtual environments isolate project dependencies.

Create:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

You should see:

```bash
(venv)
```

---

# Install FastAPI

```bash
pip install fastapi
```

---

# Install Uvicorn

Uvicorn is an ASGI server used to run FastAPI applications.

```bash
pip install uvicorn
```

---

# Verify Installation

```bash
pip list
```

You should see:

```bash
fastapi
uvicorn
```

---

# Create Main File

Create:

```bash
main.py
```

---

# Your First FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

---

# Understanding the Code

## Import FastAPI

```python
from fastapi import FastAPI
```

Imports FastAPI framework.

---

## Create Application Object

```python
app = FastAPI()
```

Creates FastAPI application instance.

Think of it as:

```python
app = MyWebsite()
```

---

## Route Decorator

```python
@app.get("/")
```

This means:

When someone visits:

```text
/
```

Execute the function below.

---

## Route Function

```python
def home():
```

Handles request.

---

## Return Response

```python
return {"message": "Hello World"}
```

FastAPI automatically converts dictionary to JSON.

Response:

```json
{
  "message": "Hello World"
}
```

---

# Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

# Understanding the Command

## main

```bash
main
```

File name:

```bash
main.py
```

---

## app

```bash
app
```

FastAPI instance:

```python
app = FastAPI()
```

---

## --reload

Automatically reloads server when code changes.

Perfect for development.

---

# Open Browser

Visit:

```text
http://127.0.0.1:8000
```

Output:

```json
{
  "message": "Hello World"
}
```

---

# Create Another Route

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/about")
def about():
    return {"message": "About Page"}
```

---

# Test

Visit:

```text
http://127.0.0.1:8000/about
```

Response:

```json
{
  "message": "About Page"
}
```

---

# Creating Multiple Endpoints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"page": "home"}

@app.get("/about")
def about():
    return {"page": "about"}

@app.get("/contact")
def contact():
    return {"page": "contact"}
```

---

# What is JSON?

JSON = JavaScript Object Notation

Used for data exchange.

Example:

```json
{
  "name": "Gaurav",
  "age": 21,
  "city": "Indore"
}
```

---

# FastAPI Automatic Documentation

One of FastAPI's best features.

---

## Swagger UI

Visit:

```text
http://127.0.0.1:8000/docs
```

You can:

- Test APIs
- View Endpoints
- Send Requests
- See Responses

Without writing frontend code.

---

## ReDoc

Visit:

```text
http://127.0.0.1:8000/redoc
```

More professional documentation view.

---

# Why Swagger is Important?

Backend developers use Swagger daily.

Benefits:

- API Testing
- Documentation
- Team Collaboration
- Frontend Integration

---

# Returning Different Data Types

## String

```python
@app.get("/hello")
def hello():
    return "Hello"
```

---

## Dictionary

```python
@app.get("/user")
def user():
    return {
        "name": "Gaurav",
        "age": 21
    }
```

---

## List

```python
@app.get("/courses")
def courses():
    return [
        "Python",
        "FastAPI",
        "Machine Learning"
    ]
```

---

# HTTP Request Lifecycle

```
User
 ↓
Request
 ↓
FastAPI Route
 ↓
Function Executes
 ↓
Response Generated
 ↓
JSON Returned
```

---

# Mini Practice Project

Create:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/student")
def student():
    return {
        "name": "Gaurav",
        "course": "BCA"
    }

@app.get("/skills")
def skills():
    return [
        "Python",
        "FastAPI",
        "SQL"
    ]
```

---

# Assignment 1

Create APIs:

```text
/
```

```text
/about
```

```text
/contact
```

```text
/services
```

---

# Assignment 2

Create Student API

Response:

```json
{
  "name": "Your Name",
  "course": "BCA",
  "semester": 6
}
```

---

# Assignment 3

Create Product API

Response:

```json
[
  {
    "id": 1,
    "name": "Laptop"
  },
  {
    "id": 2,
    "name": "Mobile"
  }
]
```

---

# Common Errors

## Error 1

```text
ModuleNotFoundError
```

Solution:

```bash
pip install fastapi
```

---

## Error 2

```text
uvicorn not found
```

Solution:

```bash
pip install uvicorn
```

---

## Error 3

```text
404 Not Found
```

Cause:

Wrong URL.

---

## Error 4

```text
IndentationError
```

Cause:

Wrong spacing.

Python uses indentation.

---

# Interview Questions

## Q1. What is FastAPI?

Answer:

FastAPI is a modern Python web framework used for building high-performance APIs. It supports automatic validation, documentation, and asynchronous programming.

---

## Q2. Why is FastAPI popular?

Answer:

Because it is:

- Fast
- Easy to use
- Automatically generates documentation
- Supports async operations
- Built using Python type hints

---

## Q3. What is Uvicorn?

Answer:

Uvicorn is an ASGI server used to run FastAPI applications.

Example:

```bash
uvicorn main:app --reload
```

---

## Q4. What is ASGI?

Answer:

ASGI stands for Asynchronous Server Gateway Interface.

It allows Python applications to handle asynchronous requests efficiently.

---

## Q5. What does app = FastAPI() do?

Answer:

It creates a FastAPI application instance that handles incoming requests.

---

## Q6. What is a Route?

Answer:

A route is a URL endpoint that executes a specific function.

Example:

```python
@app.get("/about")
```

---

## Q7. What is a Decorator?

Answer:

A decorator modifies the behavior of a function.

Example:

```python
@app.get("/")
```

Registers the function as a route.

---

## Q8. What is Swagger UI?

Answer:

Swagger UI is automatically generated API documentation available at:

```text
/docs
```

---

## Q9. What is ReDoc?

Answer:

An alternative API documentation interface available at:

```text
/redoc
```

---

## Q10. What format does FastAPI use for API responses?

Answer:

JSON (JavaScript Object Notation).

---

# Day 2 Summary

Today you learned:

✅ What FastAPI is

✅ Installing FastAPI

✅ Installing Uvicorn

✅ Creating FastAPI App

✅ Routes

✅ Decorators

✅ Running Server

✅ JSON Responses

✅ Swagger UI

✅ ReDoc

✅ Request-Response Lifecycle

✅ Basic API Development

---

# Tomorrow (Day 3)

Topics:

- Path Parameters
- Dynamic URLs
- URL Variables
- Type Validation
- Building Product APIs
- Building User APIs
- Real-world CRUD Foundation

FastAPI Journey Progress:

```text
Day 1  ❌
Day 2  ✅
Day 3  ⏳
Day 4  ⏳
Day 5  ⏳
```