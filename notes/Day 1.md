# Day 1 - Introduction to APIs & REST APIs

> FastAPI Roadmap - Day 1

---

# 🎯 Day 1 Goal

By the end of today, you will understand:

- What is an API?
- Why APIs are used
- What is a REST API?
- Client-Server Architecture
- HTTP Methods
- Request vs Response
- Status Codes
- Real-world API Examples

---

# 🤔 What is an API?

API stands for:

**Application Programming Interface**

An API acts as a messenger between two applications.

### Real-Life Example

Imagine you go to a restaurant.

- You = Client
- Waiter = API
- Kitchen = Server

Process:

1. You give your order to the waiter.
2. Waiter takes the order to the kitchen.
3. Kitchen prepares the food.
4. Waiter brings food back.

The waiter acts as the API.

---

# 💻 What Happens in Software?

Example:

You open Instagram.

- Frontend asks for posts.
- Backend receives request.
- Database sends data.
- Backend returns data.
- Frontend shows posts.

The communication happens through APIs.

---

# 📊 API Flow

```text
Client
   ↓
API Request
   ↓
Server
   ↓
Database
   ↓
Server
   ↓
API Response
   ↓
Client
```
---

# 🌍 Real-World API Examples

## Google Maps API

Used for:

- Directions
- Locations
- Distance Calculation

---

## Weather API

Used for:

- Temperature
- Humidity
- Forecast

---

## Payment API

Examples:

- Stripe
- Razorpay
- PayPal

Used for:

- Online Payments
- Transactions

---

## Social Media API

Examples:

- Instagram
- Facebook
- Twitter

Used for:

- Fetch Posts
- Upload Content
- User Authentication

---

# 🏗️ What is Client-Server Architecture?

Most modern applications follow Client-Server Architecture.

## Client

The client is the application used by users.

Examples:

- Web Browser
- Mobile App
- React Frontend

Examples:

```text
Chrome
Instagram App
React Application
```

## Server

The server processes requests and returns responses.

Examples:

```text
FastAPI
Django
Node.js
Spring Boot
```

---

# Architecture Diagram

```text
Client
(React App)

     ↓ Request

FastAPI Server

     ↓ Query

Database

     ↑ Data

FastAPI Server

     ↑ Response

Client
```

---

# 🔥 What is REST API?

REST stands for:

**Representational State Transfer**

REST is a standard way of designing APIs.

REST APIs use:

- HTTP
- URLs
- JSON

---

# Example REST API

Get all users:

```http
GET /users
```

Get a single user:

```http
GET /users/1
```

Create user:

```http
POST /users
```

Update user:

```http
PUT /users/1
```

Delete user:

```http
DELETE /users/1
```

---

# 📡 What is HTTP?

HTTP stands for:

**HyperText Transfer Protocol**

HTTP is the communication protocol between:

```text
Client ↔ Server
```

---

# HTTP Request

Example:

```http
GET /users
```

Client sends request to server.

---

# HTTP Response

Example:

```json
{
    "id": 1,
    "name": "Sauraf"
}
```

Server sends response back.

---

# 🔥 Most Important HTTP Methods

## GET

Used to fetch data.

Example:

```http
GET /users
```

Response:

```json
[
    {
        "id": 1,
        "name": "Sauraf"
    }
]
```

---

## POST

Used to create data.

Example:

```http
POST /users
```

Request Body:

```json
{
    "name": "Sauraf"
}
```

---

## PUT

Used to update complete data.

Example:

```http
PUT /users/1
```

Request:

```json
{
    "name": "Rahul"
}
```

---

## PATCH

Used to update partial data.

Example:

```http
PATCH /users/1
```

Request:

```json
{
    "name": "Rahul"
}
```

---

## DELETE

Used to remove data.

Example:

```http
DELETE /users/1
```

---

# 📨 Request vs Response

## Request

Sent by client.

Contains:

- URL
- Method
- Headers
- Body

Example:

```http
POST /users
```

---

## Response

Sent by server.

Contains:

- Status Code
- Headers
- Data

Example:

```json
{
    "message": "User Created"
}
```

---

# 🚦 HTTP Status Codes

## 200 OK

Request successful.

```http
200 OK
```

---

## 201 Created

New resource created.

```http
201 Created
```

---

## 400 Bad Request

Client sent invalid data.

```http
400 Bad Request
```

---

## 401 Unauthorized

Authentication required.

```http
401 Unauthorized
```

---

## 403 Forbidden

Access denied.

```http
403 Forbidden
```

---

## 404 Not Found

Resource does not exist.

```http
404 Not Found
```

---

## 500 Internal Server Error

Server-side error.

```http
500 Internal Server Error
```

---

# 📦 What is JSON?

JSON stands for:

**JavaScript Object Notation**

Most APIs use JSON for data exchange.

Example:

```json
{
    "id": 1,
    "name": "Sauraf",
    "age": 21,
    "city": "Indore"
}
```

---

# Why JSON?

✅ Lightweight

✅ Easy to Read

✅ Easy to Parse

✅ Language Independent

---

# 🧠 Interview Questions

## 1. What is an API?

An API is a communication bridge between two software applications.

---

## 2. What is REST API?

REST API is a web service architecture that uses HTTP methods and URLs to perform CRUD operations.

---

## 3. Difference Between API and REST API?

| API | REST API |
|-------|-------|
| General Interface | API following REST principles |
| Many Types | Uses HTTP |
| Not Always Web-Based | Web-Based |

---

## 4. What are HTTP Methods?

- GET
- POST
- PUT
- PATCH
- DELETE

---

## 5. Difference Between PUT and PATCH?

PUT updates the entire resource.

PATCH updates only specific fields.

---

## 6. What is JSON?

JSON is a lightweight data format used for API communication.

---

## 7. What is Client-Server Architecture?

A model where clients request services and servers provide responses.

---

## 8. What is Status Code 404?

Resource not found.

---

## 9. What is Status Code 500?

Internal server error.

---

## 10. What is the Purpose of GET Method?

To retrieve data from the server.

---

# 📝 Practice Questions

### Theory

1. What is API?
2. What is REST API?
3. Explain Client-Server Architecture.
4. What is HTTP?
5. Explain all HTTP methods.
6. What is JSON?
7. What is a Request?
8. What is a Response?
9. What is Status Code 201?
10. Difference between PUT and PATCH?

---

# 🚀 Day 1 Assignment

## Task 1

Draw API Architecture

```text
Client → Server → Database
```

---

## Task 2

Write examples of:

- GET
- POST
- PUT
- PATCH
- DELETE

---

## Task 3

Research and write about:

- REST API
- SOAP API
- GraphQL API

(2-3 lines each)

---

## Task 4

Find 5 APIs used in real life.

Example:

- Google Maps API
- Weather API
- Razorpay API
- PayPal API
- Instagram API

---

# 🎯 Day 1 Outcome

After completing Day 1, you should be able to:

✅ Explain APIs confidently

✅ Understand REST APIs

✅ Understand Client-Server Architecture

✅ Know HTTP Methods

✅ Understand Requests & Responses

✅ Understand Status Codes

✅ Be ready to start FastAPI coding on Day 2