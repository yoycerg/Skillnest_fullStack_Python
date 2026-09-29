import pymysql
import pymysql.cursors


class MySQLConnection:

    def __init__(self, db):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=db,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data or {})

                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                return cursor.lastrowid

            except Exception as e:
                print(f"Error MySQL: {e}")
                return False

            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)