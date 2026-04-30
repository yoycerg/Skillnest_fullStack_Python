# Instrucciones generales
# Deberá desarrollar un programa en Python que contenga un menú interactivo utilizando la estructura while, permitiendo al usuario seleccionar distintas opciones para ejecutar funciones previamente definidas.
# Cada opción del menú deberá llamar a una función diferente, la cual resolverá una situación específica utilizando distintos tipos de datos como enteros, decimales, cadenas de texto, listas y diccionarios.
# En aquellos casos donde sea necesario, deberá solicitar información al usuario mediante input(). Además, se deberá trabajar con arreglos (listas) para recorrer información utilizando ciclos for, junto con estructuras condicionales como if, elif y else.

# 1. Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def calcularMayorMenor(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número menor es: {menor}")
    print(f"El número mayor es: {mayor}")
    
def ejercicio_calcular_mayor_menor():
    limit = int(input("Ingrese la cantidad de números que desea ingresar: "))
    numeros = []
    i = 1
    while i <= limit:
        numero = int(input(f"Ingrese el número {i}: "))
        numeros.append(numero)
        i += 1
    calcularMayorMenor(numeros)
     


# 2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales


def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1

    print(f"La cadena contiene {contador} vocales.")


def ejercicio_contar_vocales():
    texto = input("Ingrese una cadena de texto: ")
    contar_vocales(texto)
    


# 3. Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.
def cincoLetras(nombre):
    return len(nombre) > 5


def filtrar_nombres(nombres):
    for nombre in nombres:
        if cincoLetras(nombre):
            print(nombre)


def filtrarNombres():
    nombres = []

    nombre1 = input("Ingrese el primer nombre: ")
    nombre2 = input("Ingrese el segundo nombre: ")
    nombre3 = input("Ingrese el tercer nombre: ")

    nombres.append(nombre1)
    nombres.append(nombre2)
    nombres.append(nombre3)

    filtrar_nombres(nombres)


# 4. Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def calcular_promedio(notas):
    if len(notas) == 0:
        print("Debe ingresar al menos una nota.")
        return

    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    print(f"El promedio es: {promedio:.1f}")

    if promedio >= 4.0:
        print("El estudiante aprueba.")
    else:
        print("El estudiante reprueba.")


def ejercicio_calcular_promedio():
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))

    if cantidad_notas <= 0:
        print("La cantidad de notas debe ser mayor a 0.")
        return 

    notas = []
    i = 1

    while i <= cantidad_notas:
        nota = float(input(f"Ingrese la nota {i}: ").replace(",", "."))
        notas.append(nota)
        i += 1

    calcular_promedio(notas)

# 5. Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * (90 / 100)
    pricioFinal = precioInicial -descuento
    print(f"El pricio inicial del producto es: \n{precioInicial} y con descuento \n{descuento}")



def valores():
    cantidadProducto = int(input("Ingrese la cantidad de producto que quieres: \n"))
    listaPrecios = []
    for i in range(cantidadProducto):
        valoresProducto = float(input("Ingrese el valor del producto:\n"))
        listaPrecios.append(valoresProducto)
    descuento(listaPrecios)    

# 6. Crear una función que reciba un número entero y determine si es par o impar.


def parImpar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es Par")
    elif numero % 3 == 0:
        print(f"El número {numero} es impar.")
    else:
        print("Error")

def recibirNum():
    num = int(input("Ingresar un número: "))
    parImpar(num)


# 7. Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
def es_mayor_edad(lista):
   num = 0
   for i in range(len(lista)):
       if lista[i] >= 18:
           num += 1
   return num

def personas():
    edad = []
    inp = int(input("¿Cuantas personas vas a ingresar hoy?:"))
    for i in range(inp):
     var = int(input(">> "))
     if var != "":
         edad.append(var)
     else:
         print("Por favor ingresar un valor válido")
resultado = edades(edad)            
              
# 8. Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabra_coincide(palabras):
    buscar = input("Ingresar la palabra que desea buscar: ")
    vecesqAperece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesqAperece += 1
    print(f"La palabra {buscar} aparece {vecesqAperece} en la lista. ")

def recibirpalabra():
    cantidad = int(input("Ingresar la cantidad de palabras: "))
    listaPalabras = []
    for i in range(cantidad):
        palabra = input(f"{i + 1}. ") 
        listaPalabras.append(palabra)
    vecesqAperece(listaPalabras)      
   

# 9. Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
def es_positivo(numero):
    pass


# 10. Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def tiene_bajo_stock(producto):
    pass


#Menu while
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular mayor y menor")
        print("2. Contar vocales")
        print("3. Filtrar nombres con más de 5 letras")
        print("4. Calcular promedio de notas")
        print("5. Aplicar descuento a precios")
        print("6. Determinar si un número es par o impar")
        print("7. Contar personas mayores de edad")
        print("8. Contar ocurrencias de una palabra")
        print("9. Filtrar números positivos")
        print("10. Mostrar productos con bajo stock")
        print("11. Salir")

        opcion = input("Seleccione una opción (1-11): ")

        if opcion == "1":
            ejercicio_calcular_mayor_menor()
        elif opcion == "2":
            ejercicio_contar_vocales()
        elif opcion == "3":
            filtrarNombres()
        elif opcion == "4":
            ejercicio_calcular_promedio()
        elif opcion == "5":
            valores()
        elif opcion == "6":
            recibirNum()
        elif opcion == "7":
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "8":
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "9":
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "10":
            pass  # Aquí se llamaría a la función correspondiente
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

menu()