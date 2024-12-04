# Python Decorators Project

This project demonstrates the practical implementation of Python decorators for database operations and query logging. It showcases how decorators can be used to enhance code reusability and maintain separation of concerns in database operations.

## Features

### 1. Query Logging Decorator (`0-log_queries.py`)
- Implements a decorator that logs SQL queries before execution
- Includes timestamp for each query execution
- Helps in debugging and monitoring database operations

### 2. Database Connection Handler (`1-with_db_connection.py`)
- Provides automatic database connection management
- Ensures proper connection closure using decorator pattern
- Reduces boilerplate code in database operations

### 3. Transaction Management (`2-transactional.py`)
- Implements automatic transaction handling
- Provides automatic commit on successful execution
- Includes automatic rollback on errors
- Ensures data consistency in database operations

## Project Structure
```
.
├── 0-log_queries.py      # Query logging decorator implementation
├── 1-with_db_connection.py   # Database connection handler
├── 2-transactional.py    # Transaction management decorator
├── create_database.py    # Database initialization script
├── data.csv             # Sample data for database population
└── users.db             # SQLite database file
```

## Usage Examples

### Query Logging
```python
@log_queries()
def fetch_all_users(query):
    # Function implementation
    pass
```

### Database Connection
```python
@with_db_connection
def get_user_by_id(conn, user_id):
    # Function implementation
    pass
```

### Transaction Management
```python
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    # Function implementation
    pass
