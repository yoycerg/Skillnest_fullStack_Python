from utils.db import get_connection

def add_favorite(user_id, book_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT IGNORE INTO favorites (user_id, book_id)
                VALUES (%s, %s)
            """, (user_id, book_id))
            return cursor.rowcount
    finally:
        connection.close()

def remove_favorite(user_id, book_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM favorites
                WHERE user_id = %s AND book_id = %s
            """, (user_id, book_id))
            return cursor.rowcount
    finally:
        connection.close()

def is_favorite(user_id, book_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 1 FROM favorites
                WHERE user_id = %s AND book_id = %s
                LIMIT 1
            """, (user_id, book_id))
            return cursor.fetchone() is not None
    finally:
        connection.close()

def get_user_favorites(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    b.id, b.title, b.author, g.name AS genre,
                    b.publication_date
                FROM favorites f
                INNER JOIN books b ON b.id = f.book_id
                INNER JOIN genres g ON g.id = b.genre_id
                WHERE f.user_id = %s
                ORDER BY f.created_at DESC
            """, (user_id,))
            return cursor.fetchall()
    finally:
        connection.close()

def get_book_favorite_users(book_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    u.id,
                    CONCAT(u.first_name, ' ', u.last_name) AS name
                FROM favorites f
                INNER JOIN users u ON u.id = f.user_id
                WHERE f.book_id = %s
                ORDER BY u.first_name, u.last_name
            """, (book_id,))
            return cursor.fetchall()
    finally:
        connection.close()
