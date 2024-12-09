#!/usr/bin/env python3
"""A module for executing database queries using context manager"""
import sqlite3


class ExecuteQuery:
    """A context manager for executing database queries"""

    def __init__(self, query, params):
        """Initialize with query and parameters"""
        self.db_name = "users.db"
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.result = None

    def __enter__(self):
        """Set up database connection and execute query"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.result = self.cursor.execute(self.query, (self.params,))
            return self.result
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection"""
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()


if __name__ == "__main__":
    # Create sample database and table
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Use the ExecuteQuery context manager
    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(query, 25) as result:
        rows = result.fetchall()
        print("Users older than 25:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
