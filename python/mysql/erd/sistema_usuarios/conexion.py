import pymysql

class Conexion:

    def __init__(self):
        self.conexion = None

    def conectar(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="usuarios_db",
            cursorclass=pymysql.cursors.DictCursor
        )
        return self.conexion

    def cerrar(self):
        if self.conexion:
            self.conexion.close()