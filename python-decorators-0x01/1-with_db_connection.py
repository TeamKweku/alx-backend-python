import sqlite3
import functools

def with_db_connection(func):
    """Decorator that handles database connection automatically.
    
    Opens a connection, passes it to the decorated function,
    and ensures the connection is properly closed afterward.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open database connection
        conn = sqlite3.connect('users.db')
        try:
            # Call the function with connection as first argument
            result = func(conn, *args, **kwargs)
            return result
        finally:
            # Ensure connection is closed even if an error occurs
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#### Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
