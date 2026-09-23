# ==========================================================
# MODELO PERSONA
# (mapea la tabla "usuarios" de esquema_usuarios)
# ==========================================================

from flask_app.config.mysqlconnection import conectar_bd

BASE_DATOS = "esquema_usuarios"


class Persona:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, registro):
        self.id = registro["id"]
        self.nombre = registro["nombre"]
        self.apellido = registro["apellido"]
        self.email = registro["email"]
        self.created_at = registro["created_at"]
        self.updated_at = registro["updated_at"]

    # ------------------------------------------------------
    # READ - todos los registros
    # ------------------------------------------------------
    @classmethod
    def obtener_todos(cls):
        sentencia = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY id;
        """

        filas = conectar_bd(BASE_DATOS).ejecutar(sentencia)

        return [cls(fila) for fila in filas] if filas else []

    # ------------------------------------------------------
    # READ - un registro por id
    # ------------------------------------------------------
    @classmethod
    def obtener_por_id(cls, id_persona):
        sentencia = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """

        parametros = {"id": id_persona}

        filas = conectar_bd(BASE_DATOS).ejecutar(sentencia, parametros)

        if filas:
            return cls(filas[0])

        return None

    # ------------------------------------------------------
    # CREATE
    # ------------------------------------------------------
    @classmethod
    def crear(cls, datos):
        sentencia = """
            INSERT INTO usuarios
                (nombre, apellido, email, created_at, updated_at)
            VALUES
                (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """

        return conectar_bd(BASE_DATOS).ejecutar(sentencia, datos)

    # ------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------
    @classmethod
    def actualizar(cls, datos):
        sentencia = """
            UPDATE usuarios
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """

        return conectar_bd(BASE_DATOS).ejecutar(sentencia, datos)

    # ------------------------------------------------------
    # DELETE
    # ------------------------------------------------------
    @classmethod
    def eliminar(cls, id_persona):
        sentencia = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """

        parametros = {"id": id_persona}

        return conectar_bd(BASE_DATOS).ejecutar(sentencia, parametros)
