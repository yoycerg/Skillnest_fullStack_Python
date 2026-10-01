from utils.db import get_connection

def create_user(first_name, last_name, email, password_hash):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO users (first_name, last_name, email, password_hash)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (first_name, last_name, email, password_hash))
            return cursor.lastrowid
    finally:
        connection.close()

def get_user_by_email(email):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE email = %s LIMIT 1",
                (email,)
            )
            return cursor.fetchone()
    finally:
        connection.close()

def get_user_by_id(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, first_name, last_name, email FROM users WHERE id = %s",
                (user_id,)
            )
            return cursor.fetchone()
    finally:
        connection.close()
