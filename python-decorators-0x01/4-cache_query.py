import time
import sqlite3
import functools

# Cache dictionary to store query results
query_cache = {}

def with_db_connection(func):
    """Decorator that handles database connection automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """Decorator that caches query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from args or kwargs
        query = kwargs.get('query')
        if not query and len(args) > 1:  # Skip first arg (conn) from with_db_connection
            query = args[1]
        
        # If query is in cache, return cached result
        if query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]
        
        # Execute function and cache result
        result = func(*args, **kwargs)
        query_cache[query] = result
        print(f"Cache miss for query: {query}")
        return result
    
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print("First call result:", users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print("Second call result:", users_again) 