from conexion import Conexion


class Usuario:

    def __init__(self):
        self.db = Conexion()

    def login(self, usuario, password):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            sql = """
            SELECT u.*, t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            WHERE usuario=%s AND password=%s
            """

            cursor.execute(sql, (usuario, password))

            return cursor.fetchone()

    def registrar(self, usuario, password, tipo):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            sql = """
            INSERT INTO usuarios(usuario,password,tipo_usuario)
            VALUES(%s,%s,%s)
            """

            cursor.execute(sql, (usuario, password, tipo))

        conexion.commit()

    def listar(self):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            sql = """
            SELECT u.id,
                   u.usuario,
                   t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            """

            cursor.execute(sql)

            return cursor.fetchall()

    def buscar(self, id):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            sql = """
            SELECT u.*,
                   t.nombre AS tipo
            FROM usuarios u
            INNER JOIN tipo_usuario t
            ON u.tipo_usuario=t.id
            WHERE u.id=%s
            """

            cursor.execute(sql, (id,))

            return cursor.fetchone()

    def modificar(self, id, usuario, password, tipo):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            sql = """
            UPDATE usuarios
            SET usuario=%s,
                password=%s,
                tipo_usuario=%s
            WHERE id=%s
            """

            cursor.execute(sql,
                           (usuario,
                            password,
                            tipo,
                            id))

        conexion.commit()

    def eliminar(self, id):

        conexion = self.db.conectar()

        with conexion.cursor() as cursor:

            cursor.execute(
                "DELETE FROM usuarios WHERE id=%s",
                (id,)
            )

        conexion.commit()