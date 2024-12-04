#!/usr/bin/python3
"""Lazy pagination module for user data"""
seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Fetch paginated user data from database
    Args:
        page_size (int): Number of records per page
        offset (int): Starting point for fetching records
    Returns:
        list: List of user records for the current page
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator function that lazily yields pages of user data
    Args:
        page_size (int): Number of records per page
    Yields:
        list: Next page of user records
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
