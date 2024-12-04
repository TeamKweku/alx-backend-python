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

def transactional(func):
    """Decorator that manages database transactions.
    
    Ensures database operations are wrapped in a transaction.
    Commits if successful, rolls back if an error occurs.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the function
            result = func(conn, *args, **kwargs)
            # If successful, commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # If an error occurs, rollback the transaction
            conn.rollback()
            raise  # Re-raise the exception after rollback
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

#### Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')