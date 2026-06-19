# Day 3: FastAPI Path Parameters & Query Parameters

## Learning Objectives

By the end of Day 3, you will be able to:

- Understand Path Parameters
- Understand Query Parameters
- Differentiate between Path and Query Parameters
- Create dynamic API routes
- Validate parameters automatically using FastAPI
- Handle optional parameters
- Build real-world API endpoints
- Answer common interview questions

---

# What are Path Parameters?

Path Parameters are values passed directly inside the URL path.

Example:

```http
GET /users/1
```

Here:

```text
1
```

is the path parameter.

The API receives the value and uses it to fetch a specific resource.

---

## Real World Examples

### Get User

```http
GET /users/1
```

### Get Product

```http
GET /products/10
```

### Get Student

```http
GET /students/5
```

---

# Creating Your First Path Parameter

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

---

## Output

Request:

```http
GET /users/10
```

Response:

```json
{
  "user_id": 10
}
```

---

# Automatic Type Conversion

FastAPI automatically converts data types.

Example:

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

Request:

```http
GET /students/20
```

Response:

```json
{
  "student_id": 20
}
```

---

# What Happens if Wrong Data Type is Passed?

Example:

```http
GET /students/abc
```

FastAPI Response:

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

FastAPI automatically validates the data.

---

# Multiple Path Parameters

Example:

```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

Request:

```http
GET /users/1/posts/10
```

Response:

```json
{
  "user_id": 1,
  "post_id": 10
}
```

---

# Path Parameters with String

Example:

```python
@app.get("/category/{category_name}")
def get_category(category_name: str):
    return {
        "category": category_name
    }
```

Request:

```http
GET /category/electronics
```

Response:

```json
{
  "category": "electronics"
}
```

---

# Path Parameters with Float

Example:

```python
@app.get("/price/{amount}")
def get_price(amount: float):
    return {
        "amount": amount
    }
```

Request:

```http
GET /price/99.99
```

Response:

```json
{
  "amount": 99.99
}
```

---

# What are Query Parameters?

Query Parameters are additional values passed after the URL.

Example:

```http
GET /products?page=1
```

Here:

```text
page=1
```

is a query parameter.

---

# Structure of Query Parameters

```http
/base-url?key=value
```

Example:

```http
/products?page=1
```

---

# Multiple Query Parameters

Example:

```http
/products?page=1&limit=10
```

---

# Creating Query Parameters

Example:

```python
@app.get("/products")
def get_products(page: int):
    return {"page": page}
```

Request:

```http
GET /products?page=2
```

Response:

```json
{
  "page": 2
}
```

---

# Multiple Query Parameters

Example:

```python
@app.get("/products")
def get_products(page: int, limit: int):
    return {
        "page": page,
        "limit": limit
    }
```

Request:

```http
GET /products?page=1&limit=20
```

Response:

```json
{
  "page": 1,
  "limit": 20
}
```

---

# Optional Query Parameters

Example:

```python
from typing import Optional

@app.get("/products")
def get_products(search: Optional[str] = None):
    return {"search": search}
```

Request:

```http
GET /products
```

Response:

```json
{
  "search": null
}
```

---

# Query Parameters with Default Values

Example:

```python
@app.get("/products")
def get_products(page: int = 1):
    return {"page": page}
```

Request:

```http
GET /products
```

Response:

```json
{
  "page": 1
}
```

---

# Real World Search API

Example:

```python
@app.get("/products")
def search_products(
    search: str = "",
    page: int = 1,
    limit: int = 10
):
    return {
        "search": search,
        "page": page,
        "limit": limit
    }
```

Request:

```http
GET /products?search=laptop&page=2&limit=5
```

Response:

```json
{
  "search": "laptop",
  "page": 2,
  "limit": 5
}
```

---

# Path Parameters vs Query Parameters

| Path Parameter | Query Parameter |
|----------|----------|
| Mandatory | Usually Optional |
| Identifies Resource | Filters Resource |
| Part of URL Path | Added After ? |
| /users/1 | /users?page=1 |

---

## Example

### Path Parameter

```http
GET /users/10
```

Get specific user.

---

### Query Parameter

```http
GET /users?page=2
```

Get filtered users.

---

# Combining Path and Query Parameters

Example:

```python
@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    show_posts: bool = False
):
    return {
        "user_id": user_id,
        "show_posts": show_posts
    }
```

Request:

```http
GET /users/1?show_posts=true
```

Response:

```json
{
  "user_id": 1,
  "show_posts": true
}
```

---

# Complete Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/products")
def get_products(
    page: int = 1,
    limit: int = 10,
    search: str = ""
):
    return {
        "page": page,
        "limit": limit,
        "search": search
    }
```

---

# Mini Project

## Student API

### Features

- Get Student By ID
- Search Student
- Pagination

---

## Example

```python
from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Amit"}
]

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}

@app.get("/students")
def get_students(
    page: int = 1,
    limit: int = 10
):
    return {
        "page": page,
        "limit": limit,
        "students": students
    }
```

---

# Common Errors

## Error 1

Wrong Data Type

```http
/students/abc
```

---

## Error 2

Missing Query Parameter

```python
def get_products(page: int)
```

Request:

```http
/products
```

Error:

```json
{
  "detail": [
    {
      "type": "missing"
    }
  ]
}
```

---

# Interview Questions

## Basic Level

### Q1. What is a Path Parameter?

Answer:

A Path Parameter is a dynamic value passed inside the URL path and is used to identify a specific resource.

Example:

```http
/users/1
```

---

### Q2. What is a Query Parameter?

Answer:

A Query Parameter is passed after the URL using `?` and is used for filtering, sorting, searching, and pagination.

Example:

```http
/products?page=1
```

---

### Q3. Difference Between Path and Query Parameters?

Answer:

| Path Parameter | Query Parameter |
|----------|----------|
| Identifies resource | Filters resource |
| Required | Optional |
| Part of URL | After ? |

---

### Q4. How does FastAPI validate parameters?

Answer:

FastAPI uses Python type hints and Pydantic validation to automatically validate incoming request data.

---

### Q5. What happens if an integer parameter receives a string?

Answer:

FastAPI automatically returns a validation error response.

---

## Intermediate Level

### Q6. Can FastAPI automatically convert data types?

Answer:

Yes.

Example:

```python
user_id: int
```

FastAPI converts the URL value into an integer automatically.

---

### Q7. Why use Query Parameters?

Answer:

For:

- Pagination
- Search
- Filtering
- Sorting

---

### Q8. Can Path and Query Parameters be used together?

Answer:

Yes.

Example:

```http
/users/1?show_posts=true
```

---

### Q9. Which parameter is better for pagination?

Answer:

Query Parameters.

Example:

```http
/products?page=1&limit=10
```

---

### Q10. Which parameter is better for fetching a specific resource?

Answer:

Path Parameters.

Example:

```http
/users/5
```

---

# Day 3 Assignment

## Task 1

Create:

```http
GET /books/{book_id}
```

Return Book ID.

---

## Task 2

Create:

```http
GET /employees/{employee_id}
```

Return Employee ID.

---

## Task 3

Create:

```http
GET /products?page=1&limit=10
```

Return pagination data.

---

## Task 4

Create:

```http
GET /search?keyword=laptop
```

Return search keyword.

---

## Task 5

Build a Student Management API using:

- Path Parameters
- Query Parameters
- Pagination
- Search

---

# Day 3 Outcome

After completing Day 3, you can:

✅ Create Dynamic Routes

✅ Use Path Parameters

✅ Use Query Parameters

✅ Validate Inputs

✅ Create Search APIs

✅ Create Pagination APIs

✅ Build Real-World Endpoints

✅ Answer FastAPI Parameter Interview Questions