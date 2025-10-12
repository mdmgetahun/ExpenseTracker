# ExpenseTracker

# Project Goal

Create a backend API for the Expense Tracker that lets users perform CRUD operations on the expense tracker app
with registration, login and other features

# Tools

* Python
* Django
* Django Rest Framework (DRF)
* Postman (for testing API endpoints)

# Main Features

User Registration
User Login with Token
Protected Endpoints (only logged-in users can create/view categories and expenses)
CRUD for Categories & Expenses

# Step by Step Development Journey

1. Starting the Idea


2. Setting Up Django Project


3. Creating Models

created models

CustomUser or default User
Category
Expense

Each category and expense must be linked to a user.

4. Serializers

serializers to convert models into JSON. For example:

RegisterSerializer
CategorySerializer
ExpenseSerializer

5. Views

API views to handle register, login, and CRUD. tested using postman

6. Authentication 

Token Authentication to protect routes so only the logged-in user can manage their own data.

7. Debugging & Fixing Errors

faced common errors like:

500 Internal Server Error
405 Method Not Allowed
URL not found (404)

Most issues were caused by missing POST methods or incorrect serializers.


# API Endpoints

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| POST   | `/api/register/`   | Create new user account |
| POST   | `/api/login/`      | Get auth token          |
| GET    | `/api/categories/` | List user categories    |
| POST   | `/api/categories/` | Create category         |
| GET    | `/api/expenses/`   | List user expenses      |
| POST   | `/api/expenses/`   | Add new expense         |
