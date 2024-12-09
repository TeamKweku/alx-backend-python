#!/usr/bin/env python3
import sqlite3


class DatabaseConnection:
    """A context manager for database connections"""

    def __init__(self, db_name="users.db"):
        """Initialize with database name"""
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Set up database connection"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            return self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection"""
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()


if __name__ == "__main__":
    # Create a sample database and table
    with DatabaseConnection() as cursor:
        # Query and print results
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print("Query Results:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}")
