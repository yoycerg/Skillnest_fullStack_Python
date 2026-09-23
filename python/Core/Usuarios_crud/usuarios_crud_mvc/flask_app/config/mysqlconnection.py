# ==========================================================
# CONEXIÓN A MYSQL
# ==========================================================

import pymysql.cursors


class ConexionBD:
    """
    Administra una conexión puntual con MySQL usando PyMySQL.
    """

    def __init__(self, nombre_bd):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=nombre_bd,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def ejecutar(self, sentencia, parametros=None):
        """
        Ejecuta una sentencia SQL (SELECT / INSERT / UPDATE / DELETE)
        y devuelve el resultado según el tipo de operación.
        """

        with self.conexion.cursor() as cursor:
            try:
                depurada = cursor.mogrify(sentencia, parametros)
                print("Ejecutando consulta:", depurada)

                cursor.execute(sentencia, parametros)

                instruccion = sentencia.strip().lower()

                if instruccion.startswith("select"):
                    return cursor.fetchall()

                if instruccion.startswith("insert"):
                    return cursor.lastrowid

                # UPDATE / DELETE
                return cursor.rowcount

            except Exception as error:
                print("Ocurrió un problema al consultar la BD:", error)
                return False

            finally:
                self.conexion.close()


def conectar_bd(nombre_bd):
    """
    Función auxiliar: crea y devuelve una instancia de ConexionBD
    para la base de datos indicada.
    """

    return ConexionBD(nombre_bd)
