from utils.db import get_connection

def get_all_books():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    b.id, b.title, b.author, b.publication_date, b.description,
                    b.user_id, b.created_at,
                    g.name AS genre,
                    CONCAT(u.first_name, ' ', u.last_name) AS owner_name,
                    (SELECT COUNT(*) FROM favorites f WHERE f.book_id = b.id) AS favorite_count
                FROM books b
                INNER JOIN genres g ON g.id = b.genre_id
                INNER JOIN users u ON u.id = b.user_id
                ORDER BY b.created_at DESC, b.id DESC
            """)
            return cursor.fetchall()
    finally:
        connection.close()

def get_book_by_id(book_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    b.id, b.title, b.author, b.genre_id, b.publication_date,
                    b.description, b.user_id, b.created_at, b.updated_at,
                    g.name AS genre,
                    CONCAT(u.first_name, ' ', u.last_name) AS owner_name
                FROM books b
                INNER JOIN genres g ON g.id = b.genre_id
                INNER JOIN users u ON u.id = b.user_id
                WHERE b.id = %s
            """, (book_id,))
            return cursor.fetchone()
    finally:
        connection.close()

def get_genres():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM genres ORDER BY name")
            return cursor.fetchall()
    finally:
        connection.close()

def create_book(title, author, genre_id, publication_date, description, user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO books
                    (title, author, genre_id, publication_date, description, user_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (title, author, genre_id, publication_date, description, user_id))
            return cursor.lastrowid
    finally:
        connection.close()

def update_book(book_id, title, author, genre_id, publication_date, description, user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE books
                SET title = %s,
                    author = %s,
                    genre_id = %s,
                    publication_date = %s,
                    description = %s,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = %s AND user_id = %s
            """, (
                title, author, genre_id, publication_date,
                description, book_id, user_id
            ))
            return cursor.rowcount
    finally:
        connection.close()

def delete_book(book_id, user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM books WHERE id = %s AND user_id = %s",
                (book_id, user_id)
            )
            return cursor.rowcount
    finally:
        connection.close()
