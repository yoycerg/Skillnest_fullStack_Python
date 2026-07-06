from usuario import Usuario

usuario = Usuario()

while True:

    print("========================")
    print(" SISTEMA DE USUARIOS")
    print("========================")
    print("1. Iniciar sesión")
    print("2. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":

        user = input("Usuario: ")
        password = input("Contraseña: ")

        datos = usuario.login(user, password)

        if datos is None:
            print("Usuario o contraseña incorrectos")
            continue

        if datos["tipo"] == "ADMIN":

            while True:

                print("\nAdministrador:", datos["usuario"])
                print("1. Registrar")
                print("2. Listar")
                print("3. Buscar")
                print("4. Modificar")
                print("5. Eliminar")
                print("6. Cerrar sesión")

                op = input()

                if op == "1":

                    u = input("Usuario: ")
                    p = input("Password: ")
                    t = input("Tipo (1 ADMIN /2 USER): ")

                    usuario.registrar(u, p, t)

                    print("Usuario registrado")

                elif op == "2":

                    lista = usuario.listar()

                    print()

                    for x in lista:
                        print(
                            x["id"],
                            x["usuario"],
                            x["tipo"]
                        )

                elif op == "3":

                    id = input("ID: ")

                    datos = usuario.buscar(id)

                    print(datos)

                elif op == "4":

                    id = input("ID: ")
                    u = input("Nuevo usuario: ")
                    p = input("Nuevo password: ")
                    t = input("Tipo: ")

                    usuario.modificar(id, u, p, t)

                    print("Actualizado")

                elif op == "5":

                    id = input("ID: ")

                    usuario.eliminar(id)

                    print("Eliminado")

                elif op == "6":
                    break

        else:

            while True:

                print("\nBienvenido")
                print(datos["usuario"])
                print("Tipo:", datos["tipo"])
                print("1. Cerrar sesión")

                op = input()

                if op == "1":
                    break

    elif opcion == "2":
        break