# Python Generators Project

This project demonstrates the use of Python generators and MySQL database operations. The main script `seed.py` sets up a MySQL database and populates it with user data.

## Requirements
- Python 3.x
- MySQL
- Required Python packages:
  - mysql-connector-python
  - sqlalchemy
  - sqlalchemy-utils
  - pandas (for reading CSV data)
  - uuid

## Project Structure
- `seed.py`: Main script containing database setup and data insertion functions (using mysql-connector)
- `seed_sqlalchemy.py`: Alternative implementation using SQLAlchemy ORM
- `user_data.csv`: Sample data file containing user information

## Functions
1. `connect_db()`: Connects to MySQL server
2. `create_database(connection)`: Creates ALX_prodev database
3. `connect_to_prodev()`: Connects to ALX_prodev database
4. `create_table(connection)`: Creates user_data table
5. `insert_data(connection, data)`: Inserts data from CSV file

## Database Schema
Table: user_data
- user_id (UUID, Primary Key, Indexed)
- name (VARCHAR, NOT NULL)
- email (VARCHAR, NOT NULL)
- age (DECIMAL, NOT NULL)
