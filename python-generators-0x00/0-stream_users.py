#!/usr/bin/python3
import mysql.connector


def stream_users():
    """Generator function that yields rows from user_data table one by one"""
    # Database configuration
    DB_CONFIG = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "mysecretpassword",
        "database": "ALX_prodev",
    }

    connection = None
    cursor = None
    try:
        # Connect to database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True, buffered=True)

        # Execute query and yield rows one by one
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        yield None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
