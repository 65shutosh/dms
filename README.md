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

## License

This project is licensed under the MIT License. 