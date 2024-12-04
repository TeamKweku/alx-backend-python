# Python Generators Project

This project demonstrates advanced use of Python generators for efficient data processing and MySQL database operations. It implements various generator patterns for streaming, batch processing, pagination, and memory-efficient data aggregation.

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

### Database Setup
- `seed.py`: Database setup and data seeding script
- `data.csv`: Sample user data with 200 entries

### Generator Implementations
1. `0-stream_users.py`: Basic user data streaming
   - Implements generator to stream user records
   - Memory-efficient data retrieval
   - Proper database connection handling

2. `1-batch_processing.py`: Batch data processing
   - Processes user data in configurable batches
   - Filters users over age 25
   - Uses yield generator with maximum 2 loops

3. `2-lazy_paginate.py`: Lazy pagination
   - Implements lazy loading of paginated data
   - Uses single loop with yield generator
   - Efficient memory usage with cursor-based pagination

4. `4-stream_ages.py`: Memory-efficient aggregation
   - Streams user ages one at a time
   - Calculates average age without loading entire dataset
   - Uses maximum two loops
   - Pure Python implementation (no SQL aggregation)

## Database Schema
Table: user_data
- user_id (UUID, Primary Key, Indexed)
- name (VARCHAR, NOT NULL)
- email (VARCHAR, NOT NULL, UNIQUE)
- age (DECIMAL, NOT NULL)

## Key Features
1. Generator-based Data Processing
   - Memory efficient data handling
   - Lazy evaluation of data
   - Proper resource management

2. Batch Processing
   - Configurable batch sizes
   - Age-based filtering
   - Generator-based implementation

3. Pagination Support
   - Lazy loading of pages
   - Cursor-based pagination
   - Memory-efficient page retrieval

4. Efficient Aggregation
   - Streaming calculation of averages
   - Minimal memory footprint
   - Pure Python implementation

## Usage Examples

### Stream Users
```python
for user in stream_users():
    print(user)
```

### Batch Processing
```python
for batch in batch_processing(100):
    # Process users over 25
    print(batch)
```

### Lazy Pagination
```python
for page in lazy_pagination(50):
    for user in page:
        print(user)
```

### Calculate Average Age
```python
average_age = calculate_average_age()
print(f"Average age of users: {average_age:.2f}")
```

## Best Practices Implemented
1. Proper database connection handling
2. Memory-efficient data processing
3. Generator-based lazy evaluation
4. Clean code with proper documentation
5. Modular design with single responsibility
6. Error handling and resource cleanup
