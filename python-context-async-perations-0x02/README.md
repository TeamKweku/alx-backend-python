# Context Managers and Asynchronous Programming in Python

This project demonstrates the implementation and usage of context managers and asynchronous programming patterns in Python, specifically focused on database operations using SQLite.

## Project Overview

The project consists of three main components that showcase different approaches to database handling:

1. **Basic Database Connection Manager** (`0-databaseconnection.py`)
   - Implements a context manager for handling SQLite database connections
   - Provides automatic connection handling and resource cleanup
   - Demonstrates the use of `__enter__` and `__exit__` methods

2. **Query Execution Manager** (`1-execute.py`)
   - Extends the context manager pattern for specific query execution
   - Handles parameterized queries safely
   - Includes automatic transaction management

3. **Asynchronous Database Operations** (`3-concurrent.py`)
   - Demonstrates modern async/await syntax with SQLite
   - Uses `aiosqlite` for asynchronous database operations
   - Shows concurrent execution of multiple queries

## Features

- Context manager implementation for safe database handling
- Automatic resource cleanup and connection management
- Transaction handling with commit/rollback support
- Asynchronous database operations
- Concurrent query execution
- Error handling and logging

## Usage Examples

### Basic Database Connection
```python
with DatabaseConnection() as cursor:
    cursor.execute("SELECT FROM users")
    results = cursor.fetchall()
```
### Parameterized Query Executin
```python
query = "SELECT FROM users WHERE age > ?"
with ExecuteQuery(query, 25) as result:
    rows = result.fetchall()
```


### Asynchronous Operations
```python
async def main():
    users, older_users = await fetch_concurrently()
    print("All users:", users)
    print("Older users:", older_users)

asyncio.run(main())
```

## Requirements

- Python 3.10+
- sqlite3
- aiosqlite

## Project Structure

- `0-databaseconnection.py`: Basic database connection context manager
- `1-execute.py`: Query execution context manager
- `3-concurrent.py`: Asynchronous database operations
- `users.db`: SQLite database file (created at runtime)

## Best Practices Demonstrated

- Resource management using context managers
- Separation of concerns
- Error handling and logging
- Modern async/await patterns
- Concurrent operations
- Safe database transaction handling

## License

This project is open source and available under the MIT License.