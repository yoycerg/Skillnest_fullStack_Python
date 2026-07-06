from datetime import datetime

class Usuario:
    usuarios = []

    def __init__(self, nombre_usuario, password, email, rol):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.email = email
        self.rol = rol
        self.fecha_creacion = datetime.now().strftime("%d/%m/%Y %H:%M")
        Usuario.usuarios.append(self)

    def mostrar_datos(self):
        print(f"""
        Nombre Usuario: {self.nombre_usuario}
        Rol: {self.rol}
        Fecha Creación: {self.fecha_creacion}""")

    def actualizar_correo(self, nuevo_correo):
        self.email = nuevo_correo
        print("Correo actualizado correctamente")

class Autor:
    def __init__(self, nombre_autor, apellido_autor, nacionalidad, correo):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.nacionalidad = nacionalidad
        self.correo = correo

    def mostrar_autor(self):
        print(f"""
        Autor: {self.nombre_autor} {self.apellido_autor}
        Nacionalidad: {self.nacionalidad}
        Correo: {self.correo}""")

class Libro:
    def __init__(self, titulo, descripcion, fecha_publicacion, categoria, autor):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.categoria = categoria
        self.autor = autor
        self.disponible = True

    def mostrar_informacion(self):
        print(f"""
        Título: {self.titulo}
        Descripción: {self.descripcion}
        Fecha Publicación: {self.fecha_publicacion}
        Categoría: {self.categoria}
        Disponible: {self.disponible}
        Autor: {self.autor.nombre_autor} {self.autor.apellido_autor}""")

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro

    def registrar_prestamo(self):
        if self.libro.disponible:
            self.libro.disponible = False
            print(f"""
            Préstamo registrado correctamente
            Usuario: {self.usuario.nombre_usuario}
            Libro: {self.libro.titulo}""")
        else:
            print("El libro no está disponible")

    def devolver_libro(self):
        self.libro.disponible = True
        print(f"""
        Libro devuelto correctamente
        Libro: {self.libro.titulo}
""")

roles = ["Administrador", "Bibliotecario", "Usuario"]
        
libros = []
prestamos = []
autores = []

def main():
    continuar = True

    while continuar:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1.- Crear usuario")
        print("2.- Mostrar usuarios")
        print("3.- Crear autor")
        print("4.- Crear libro")
        print("5.- Mostrar libros")
        print("6.- Crear préstamo")
        print("7.- Buscar usuario")
        print("8.- Devolver libro")
        print("0.- Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            nombre_usuario = input("Ingrese nombre de usuario: ")
            password = input("Ingrese password: ")
            email = input("Ingrese email: ")

            print("\n--- ROLES DISPONIBLES ---")

            for i, rol in enumerate(roles):
                print(f"{i}.- {rol}")

            indice_rol = int(input("Seleccione rol: "))

            if 0 <= indice_rol < len(roles):
                rol_seleccionado = roles[indice_rol]

                Usuario(
                    nombre_usuario,
                    password,
                    email,
                    rol_seleccionado
                )

                print("Usuario creado correctamente.")
            else:
                print("Rol inválido")

        elif opcion == "2":
            print("\n--- LISTA DE USUARIOS ---")

            if len(Usuario.usuarios) == 0:
                print("No hay usuarios registrados")
            else:
                for usuario in Usuario.usuarios:
                    usuario.mostrar_datos()

        elif opcion == "3":
            nombre_autor = input("Ingrese nombre del autor: ")
            apellido_autor = input("Ingrese apellido del autor: ")
            nacionalidad = input("Ingrese nacionalidad: ")
            correo = input("Ingrese correo: ")

            autor = Autor(
                nombre_autor,
                apellido_autor,
                nacionalidad,
                correo
            )

            autores.append(autor)

            print("Autor creado correctamente.")

        elif opcion == "4":
            if len(autores) == 0:
                print("Debe crear un autor primero.")
            else:
                titulo = input("Ingrese título: ")
                descripcion = input("Ingrese descripción: ")
                fecha = input("Ingrese fecha publicación: ")
                categoria = input("Ingrese categoría: ")

                print("\n--- AUTORES DISPONIBLES ---")

                for i, autor in enumerate(autores):
                    print(f"{i}.- {autor.nombre_autor} {autor.apellido_autor}")

                indice_autor = int(input("Seleccione autor: "))

                if 0 <= indice_autor < len(autores):
                    autor_seleccionado = autores[indice_autor]

                    libro = Libro(
                        titulo,
                        descripcion,
                        fecha,
                        categoria,
                        autor_seleccionado
                    )

                    libros.append(libro)

                    print("Libro creado correctamente.")
                else:
                    print("Autor inválido")

        elif opcion == "5":
            print("\n--- LISTA DE LIBROS ---")

            if len(libros) == 0:
                print("No hay libros registrados")
            else:
                for libro in libros:
                    libro.mostrar_informacion()

        elif opcion == "6":
            if len(Usuario.usuarios) == 0 or len(libros) == 0:
                print("Debe existir al menos un usuario y un libro.")
            else:
                print("\n--- USUARIOS ---")

                for i, usuario in enumerate(Usuario.usuarios):
                    print(f"{i}.- {usuario.nombre_usuario} - {usuario.rol}")

                indice_usuario = int(input("Seleccione usuario: "))

                print("\n--- LIBROS ---")

                for i, libro in enumerate(libros):
                    print(f"{i}.- {libro.titulo}")

                indice_libro = int(input("Seleccione libro: "))

                if 0 <= indice_usuario < len(Usuario.usuarios) and 0 <= indice_libro < len(libros):
                    usuario = Usuario.usuarios[indice_usuario]
                    libro = libros[indice_libro]

                    prestamo = Prestamo(usuario, libro)

                    prestamos.append(prestamo)

                    prestamo.registrar_prestamo()
                else:
                    print("Datos inválidos")

        elif opcion == "7":
            nombre_buscar = input("Ingrese nombre de usuario: ")

            encontrado = False

            for usuario in Usuario.usuarios:
                if usuario.nombre_usuario == nombre_buscar:
                    usuario.mostrar_datos()
                    encontrado = True

            if encontrado == False:
                print("Usuario no encontrado")

        elif opcion == "8":
            if len(prestamos) == 0:
                print("No existen préstamos")
            else:
                print("\n--- PRÉSTAMOS ---")

                for i, prestamo in enumerate(prestamos):
                    print(f"{i}.- {prestamo.usuario.nombre_usuario} - {prestamo.libro.titulo}")

                indice = int(input("Seleccione préstamo: "))

                if 0 <= indice < len(prestamos):
                    prestamos[indice].devolver_libro()
                else:
                    print("Préstamo inválido")

        elif opcion == "0":
            print("Saliendo del sistema...")
            continuar = False

        else:
            print("Opción inválida")

main()