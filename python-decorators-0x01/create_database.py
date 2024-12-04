import sqlite3
import csv

def create_and_populate_db():
    # Create connection to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    ''')

    # Read CSV and insert data
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (row['name'], row['email'], int(row['age'])))
    except FileNotFoundError:
        print("Error: data.csv file not found!")
        return

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database created and populated successfully!")

if __name__ == "__main__":
    create_and_populate_db() 