#!/usr/bin/python3
"""Module for batch processing user data from MySQL database"""
import mysql.connector


def stream_users_in_batches(batch_size):
    """Generator function that yields rows in batches from user_data table"""
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
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True, buffered=True)

        # Execute query to get all users
        cursor.execute("SELECT * FROM user_data")
        
        # Fetch and yield batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """Process batches and filter users over age 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user['age']) > 25:
                print(user)
