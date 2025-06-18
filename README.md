# Delivery Management System (DMS)

A professional backend system for managing deliveries, built with FastAPI.

## Features

- Secure authentication and authorization
- User management
- Delivery tracking
- Order management
- Real-time status updates
- API documentation with Swagger UI

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic for migrations
- JWT for authentication
- Pydantic for data validation

## Project Structure

```
dms/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Core functionality
│   ├── db/           # Database models and session
│   ├── models/       # SQLAlchemy models
│   ├── schemas/      # Pydantic schemas
│   ├── services/     # Business logic
│   └── utils/        # Utility functions
├── tests/            # Test cases
└── alembic/          # Database migrations
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dms
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Run migrations:
```bash
alembic upgrade head
```

5. Start the server:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS middleware
- Rate limiting
- Input validation
- SQL injection prevention
- XSS protection

## Testing

Run tests using pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Library Summary

| **Library**        | **Used/Required?** | **Notes**                              |
| ------------------ | ------------------ | -------------------------------------- |
| alembic            | Yes                | Migrations                             |
| annotated-types    | Indirect           | Only as a dependency, not in your code |
| anyio              | Indirect           | Dependency of FastAPI/Starlette        |
| bcrypt             | Yes                | Via passlib                            |
| certifi            | Indirect           | Dependency of httpx                    |
| cffi               | Indirect           | Dependency of cryptography             |
| click              | Indirect           | Dependency of alembic                  |
| colorama           | Indirect           | Dependency of click                    |
| cryptography       | Yes                | Used by python-jose/passlib            |
| dnspython          | Indirect           | Used by email\_validator               |
| ecdsa              | No                 | No evidence of use                     |
| email\_validator   | Yes                | Used for email validation              |
| fastapi            | Yes                | Main framework                         |
| greenlet           | Indirect           | Dependency of SQLAlchemy               |
| h11                | Indirect           | Dependency of httpx/uvicorn            |
| httpcore           | Indirect           | Dependency of httpx                    |
| httpx              | Indirect           | Used by FastAPI                        |
| idna               | Indirect           | Dependency of httpx/email\_validator   |
| iniconfig          | Indirect           | Used by pytest                         |
| Mako               | Indirect           | Used by alembic                        |
| MarkupSafe         | Indirect           | Used by Mako                           |
| packaging          | Indirect           | Used by pytest/pydantic                |
| passlib            | Yes                | Used for password hashing              |
| pluggy             | Indirect           | Used by pytest                         |
| psycopg2-binary    | Yes                | PostgreSQL driver                      |
| pyasn1             | Indirect           | Used by cryptography                   |
| pycparser          | Indirect           | Used by cffi                           |
| pydantic           | Yes                | Used for data validation               |
| pydantic-settings  | Yes                | Used for settings                      |
| pydantic\_core     | Indirect           | Used by pydantic                       |
| Pygments           | Indirect           | Used by pytest                         |
| pytest             | Yes                | For testing                            |
| python-dotenv      | Yes                | For environment variables              |
| python-jose        | Yes                | For JWT                                |
| python-multipart   | Yes                | For file uploads                       |
| rsa                | Indirect           | Used by python-jose                    |
| six                | Indirect           | Used by dependencies                   |
| sniffio            | Indirect           | Used by httpx                          |
| SQLAlchemy         | Yes                | ORM                                    |
| starlette          | Indirect           | Used by FastAPI                        |
| typing-inspection  | Indirect           | Used by pydantic                       |
| typing\_extensions | Indirect           | Used by pydantic/FastAPI               |
| uvicorn            | Yes                | ASGI server                            |




## License

This project is licensed under the MIT License. 
