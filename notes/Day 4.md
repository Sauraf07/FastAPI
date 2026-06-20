# Day 4 - FastAPI Path Parameters & Query Parameters

> Goal: Learn how to receive data from URLs using Path Parameters and Query Parameters, validate them, and build real-world APIs.

---

# What You Will Learn Today

- What are Path Parameters?
- What are Query Parameters?
- Difference Between Path and Query Parameters
- Type Validation
- Optional Parameters
- Default Values
- Multiple Query Parameters
- Parameter Validation
- Real-World Examples
- Common Mistakes
- Interview Questions

---

# What is a Path Parameter?

A Path Parameter is a value that is part of the URL path.

Example:

```url
/users/1
/products/10
/students/101
```

In the above URLs:

```text
1
10
101
```

are Path Parameters.

---

# Why Use Path Parameters?

Path Parameters are used when you want to access a specific resource.

Examples:

```url
/users/1
/products/100
/orders/25
```

Meaning:

```text
Get User with ID 1
Get Product with ID 100
Get Order with ID 25
```

---

# Creating Your First Path Parameter

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}
```

---

## Run Server

```bash
uvicorn main:app --reload
```

Open:

```url
http://127.0.0.1:8000/users/10
```

Output:

```json
{
  "user_id": "10"
}
```

Notice:

```text
10 is returned as string
```

because FastAPI doesn't know the datatype yet.

---

# Type Validation

FastAPI automatically validates data types.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

---

### Valid Request

```url
/users/10
```

Response:

```json
{
  "user_id": 10
}
```

---

### Invalid Request

```url
/users/abc
```

Response:

```json
{
  "detail": [
    {
      "type": "int_parsing"
    }
  ]
}
```

FastAPI automatically validates input.

---

# Path Parameters with Multiple Values

```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

Request:

```url
/users/1/posts/100
```

Response:

```json
{
  "user_id": 1,
  "post_id": 100
}
```

---

# Different Data Types

## Integer

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}
```

---

## Float

```python
@app.get("/price/{amount}")
def get_price(amount: float):
    return {"amount": amount}
```

Request:

```url
/price/99.99
```

---

## String

```python
@app.get("/student/{name}")
def get_student(name: str):
    return {"name": name}
```

---

# What are Query Parameters?

Query Parameters are values passed after the `?` symbol.

Example:

```url
/products?page=1
/products?page=1&limit=10
/products?category=laptop
```

---

# Why Use Query Parameters?

Used for:

- Filtering
- Searching
- Pagination
- Sorting

Examples:

```text
Search Product
Filter Users
Pagination
Sort Data
```

---

# Basic Query Parameter Example

```python
@app.get("/products")
def get_products(page: int):
    return {"page": page}
```

Request:

```url
/products?page=2
```

Response:

```json
{
  "page": 2
}
```

---

# Query Parameter with Default Value

```python
@app.get("/products")
def get_products(page: int = 1):
    return {"page": page}
```

Request:

```url
/products
```

Output:

```json
{
  "page": 1
}
```

---

# Multiple Query Parameters

```python
@app.get("/products")
def get_products(
    page: int = 1,
    limit: int = 10
):
    return {
        "page": page,
        "limit": limit
    }
```

Request:

```url
/products?page=2&limit=5
```

Output:

```json
{
  "page": 2,
  "limit": 5
}
```

---

# Optional Query Parameters

```python
from typing import Optional

@app.get("/search")
def search_product(name: Optional[str] = None):
    return {"name": name}
```

Request:

```url
/search
```

Output:

```json
{
  "name": null
}
```

---

Request:

```url
/search?name=laptop
```

Output:

```json
{
  "name": "laptop"
}
```

---

# Real-World Search API

```python
@app.get("/products")
def search_products(
    keyword: str = "",
    page: int = 1,
    limit: int = 10
):
    return {
        "keyword": keyword,
        "page": page,
        "limit": limit
    }
```

Request:

```url
/products?keyword=iphone&page=2&limit=20
```

Response:

```json
{
  "keyword": "iphone",
  "page": 2,
  "limit": 20
}
```

---

# Combining Path and Query Parameters

```python
@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    active: bool = True
):
    return {
        "user_id": user_id,
        "active": active
    }
```

Request:

```url
/users/10?active=false
```

Output:

```json
{
  "user_id": 10,
  "active": false
}
```

---

# Path Parameter vs Query Parameter

| Feature | Path Parameter | Query Parameter |
|----------|----------|----------|
| Location | URL Path | After ? |
| Purpose | Specific Resource | Filtering/Search |
| Required | Usually Yes | Usually Optional |
| Example | /users/1 | ?page=1 |

---

# Common Mistakes

## Mistake 1

```python
@app.get("/users/{id}")
def get_user(id):
```

No datatype specified.

Better:

```python
@app.get("/users/{id}")
def get_user(id: int):
```

---

## Mistake 2

Using query parameter for resource identification.

Wrong:

```url
/users?id=1
```

Better:

```url
/users/1
```

---

## Mistake 3

Not providing default values.

Wrong:

```python
def get_products(page: int):
```

Better:

```python
def get_products(page: int = 1):
```

---

# Mini Project

## Student Management API

### Endpoints

### Get Student

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }
```

---

### Search Student

```python
@app.get("/students")
def search_student(
    name: str = "",
    page: int = 1
):
    return {
        "name": name,
        "page": page
    }
```

---

# Practice Exercises

## Beginner

1. Create Product API
2. Create Student API
3. Create Employee API
4. Create Book API
5. Create Order API

---

## Intermediate

1. Product Search API
2. Pagination API
3. User Filter API
4. Blog Search API
5. Student Search API

---

# Interview Questions

## Q1 What is a Path Parameter?

Answer:

A Path Parameter is a variable part of a URL used to identify a specific resource.

Example:

```url
/users/1
```

---

## Q2 What is a Query Parameter?

Answer:

A Query Parameter is used for filtering, searching, sorting, or pagination.

Example:

```url
/products?page=1
```

---

## Q3 Difference Between Path and Query Parameters?

Answer:

Path Parameters identify resources.

Example:

```url
/users/1
```

Query Parameters filter or modify data.

Example:

```url
/users?page=1
```

---

## Q4 How does FastAPI validate Path Parameters?

Answer:

Using Python type hints.

Example:

```python
user_id: int
```

FastAPI automatically validates the datatype.

---

## Q5 Can Query Parameters Have Default Values?

Answer:

Yes.

Example:

```python
page: int = 1
```

---

## Q6 Are Query Parameters Required?

Answer:

No.

They can be optional by providing default values.

---

## Q7 Can We Use Path and Query Parameters Together?

Answer:

Yes.

Example:

```url
/users/1?active=true
```

---

## Q8 What Happens If Wrong Datatype Is Passed?

Answer:

FastAPI automatically returns a validation error.

Example:

```url
/users/abc
```

Returns:

```json
422 Validation Error
```

---

## Q9 Why is FastAPI Better Than Flask for Validation?

Answer:

Because FastAPI automatically validates inputs using Python type hints and Pydantic.

---

## Q10 What HTTP Status Code Does FastAPI Return for Validation Errors?

Answer:

```text
422 Unprocessable Entity
```

---

# Day 4 Summary

Today you learned:

✅ Path Parameters

✅ Query Parameters

✅ Type Validation

✅ Optional Parameters

✅ Default Values

✅ Multiple Parameters

✅ Path vs Query Parameters

✅ Real-World Search APIs

✅ Interview Questions

---

# Tomorrow (Day 5)

Topics:

- Request Body
- Pydantic Models
- POST APIs
- Data Validation
- Create User API
- CRUD Foundation

You will start building real APIs that accept JSON data from clients.