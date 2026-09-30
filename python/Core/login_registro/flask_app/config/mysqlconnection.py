import pymysql.cursors

# ---- Ajusta estos datos a tu MySQL local ----
DB_USER = "root"
DB_PASSWORD = "1234"      # <- pon tu contraseña de MySQL
DB_HOST = "localhost"
DB_PORT = 3306
# ---------------------------------------------


class MySQLConnection:
    def __init__(self, db):
        self.connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,
        )

    def query_db(self, query, data=None):
        """SELECT -> lista de diccionarios | INSERT -> id insertado | otros -> None"""
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                if query.lstrip().lower().startswith("select"):
                    return cursor.fetchall()
                self.connection.commit()
                if query.lstrip().lower().startswith("insert"):
                    return cursor.lastrowid
                return None
            except Exception as e:
                print("Error en la consulta:", e)
                self.connection.rollback()
                return False
            finally:
                self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)
