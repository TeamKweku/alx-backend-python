import sqlite3
import functools

def log_queries():
    """Decorator that logs the SQL query before executing it"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Extract query from args or kwargs
            query = kwargs.get('query') or args[0]
            # Log the query
            print(f"Query: {query}")
            # Execute the function
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results 

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")