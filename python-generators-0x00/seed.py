#!/usr/bin/python3
"""
Module for setting up and populating MySQL database
"""
import csv
import os
import uuid
from typing import Optional

import mysql.connector

# Database configuration
DB_CONFIG = {
    "host": "localhost",  # Docker container is mapped to localhost
    "port": 3306,  # Port exposed by Docker
    "user": "root",  # Default MySQL user
    "password": "mysecretpassword",  # Your MySQL root password
}


def connect_db() -> Optional[mysql.connector.MySQLConnection]:
    """Connects to the MySQL database server"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def create_database(connection: mysql.connector.MySQLConnection) -> None:
    """Creates the ALX_prodev database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")


def connect_to_prodev() -> Optional[mysql.connector.MySQLConnection]:
    """Connects to the ALX_prodev database"""
    try:
        config = DB_CONFIG.copy()
        config["database"] = "ALX_prodev"
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None


def create_table(connection: mysql.connector.MySQLConnection) -> None:
    """Creates the user_data table if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age DECIMAL NOT NULL,
                INDEX idx_user_id (user_id)
            )
        """
        )
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


def insert_data(connection: mysql.connector.MySQLConnection, data: str) -> None:
    """Inserts data from CSV file into the database"""
    try:
        if not os.path.exists(data):
            print(f"Error: Data file {data} not found")
            return

        cursor = connection.cursor()

        with open(data, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                user_id = str(uuid.uuid4())

                # Check if record already exists
                cursor.execute(
                    "SELECT user_id FROM user_data WHERE user_id = %s",
                    (row["email"],),
                )
                if not cursor.fetchone():
                    cursor.execute(
                        """
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """,
                        (
                            user_id,
                            row["name"],
                            row["email"],
                            float(row["age"]),  # Convert to float if needed
                        ),
                    )

        connection.commit()
        cursor.close()
    except (mysql.connector.Error, csv.Error, IOError) as err:
        print(f"Error inserting data: {err}")

