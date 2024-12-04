#!/usr/bin/python3
"""Memory-efficient age aggregation using generators"""
seed = __import__('seed')


def stream_user_ages():
    """
    Generator that yields user ages one at a time
    Yields:
        int: Age of each user
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    # Use cursor as iterator to avoid loading all records at once
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield int(row['age'])

    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Calculate average age using the stream_user_ages generator
    Returns:
        float: Average age of all users
    """
    total_age = 0
    count = 0

    # Use generator to process ages one at a time
    for age in stream_user_ages():
        total_age += age
        count += 1

    return total_age / count if count > 0 else 0


if __name__ == "__main__":
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
