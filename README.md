# 🚀 AuthHub API

A production-ready Authentication & Product Management REST API built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**.

Designed to demonstrate backend engineering skills including authentication, authorization, database design, secure password hashing, and CRUD API development.

---

## 🌍 Live Demo

### API
https://authhub-api.onrender.com/

### Interactive Swagger Documentation
https://authhub-api.onrender.com/docs

---

# Features

## Authentication

- User Registration
- User Login
- JWT Access Tokens
- OAuth2 Password Flow
- Password Hashing (bcrypt)

---

## User Management

- Register new users
- Login existing users
- Retrieve authenticated user information

---

## Product Management

Authenticated users can:

- Create Products
- View All Products
- View Single Product
- Update Products
- Delete Products

Each product is linked to its owner.

---

# Tech Stack

### Backend

- Python 3
- FastAPI
- SQLAlchemy (Async ORM)
- PostgreSQL
- Pydantic
- Uvicorn

### Authentication

- JWT (python-jose)
- OAuth2 Password Flow
- Passlib + bcrypt

### Deployment

- Render
- PostgreSQL (Render Database)

---

# API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |

---

## Users

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/users/me` | Get Current Authenticated User |

---

## Products

| Method | Endpoint |
|---------|----------|
| GET | `/products/` |
| POST | `/products/` |
| GET | `/products/{id}` |
| PUT | `/products/{id}` |
| DELETE | `/products/{id}` |

---

# Authentication Flow

1. Register an account

```
POST /auth/register
```

↓

2. Login

```
POST /auth/login
```

↓

3. Receive JWT Token

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

↓

4. Click **Authorize** in Swagger Docs

↓

5. Access Protected Routes

---

# Installation

Clone the repository

```bash
git clone https://github.com/EmmanuelOmoruyi/AuthHub-API.git
```

Move into the project

```bash
cd AuthHub
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Visit

```
http://127.0.0.1:8000/docs
```

---

# Environment Variables

Create a `.env`

```env
DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Project Structure

```
app
│
├── core
│   ├── oauth2.py
│   └── security.py
│
├── db
│   └── database.py
│
├── models
│   ├── user.py
│   └── product.py
│
├── routes
│   ├── auth.py
│   ├── users.py
│   └── products.py
│
├── schemas
│   ├── user.py
│   ├── product.py
│   └── token.py
│
└── main.py
```

---

# Example Product Response

```json
{
    "id": 1,
    "title": "MacBook Pro",
    "description": "Professional laptop",
    "price": 1999.99,
    "owner_id": 1
}
```

---

# Security

- Passwords are hashed using bcrypt.
- JWT Authentication protects secured endpoints.
- OAuth2 Password Bearer is used for authorization.
- User identity is extracted from JWT tokens before protected operations.

---

# Future Improvements

- Docker Support
- Alembic Database Migrations
- Pagination
- Product Search
- Product Categories
- Image Uploads
- Unit Testing
- CI/CD Pipeline
- Role-Based Authorization (Admin/User)
- Refresh Tokens
- Email Verification

---

# Skills Demonstrated

- REST API Design
- Authentication & Authorization
- JWT
- OAuth2
- Async SQLAlchemy
- PostgreSQL
- FastAPI
- CRUD Operations
- Database Relationships
- Secure Password Storage
- API Deployment
- Production API Documentation

---

# Author

**Emmanuel Omoruyi**

Backend Developer

GitHub:
https://github.com/EmmanuelOmoruyi/AuthHub-API

LinkedIn:
(https://www.linkedin.com/in/emmanuel-omoruyi-387666405/)

---

## ⭐ If you found this project interesting, consider giving it a star!
