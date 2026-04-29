#1- Crear una función que reciba una lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
def numeroMayorMenor(lista):
    menor = min(lista)
    mayor = max(lista)
    print(f"El número mayor es {mayor}nEl número menor es: {menor}")
def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listaNum = []
    i = i
    while i <= limit:
        num = input("Ingresa un numero entero o decimal (con punto): ")
        listaNum.append(num)
        i+=1
    numeroMayorMenor(listaNum)       

#2- Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
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
    

#3- Crear una función que reciba una lista de nombres y muestre únicamente aquellos que tengan más de 5 letras.





#4- Crear una función que reciba una lista de notas (números decimales), calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
#5- Crear una función que reciba una lista de precios de productos y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
#6- Crear una función que reciba un número entero y determine si es par o impar.
#7- Crear una función que reciba una lista de edades y muestre cuántas personas son mayores de edad (18 años o más).
#8- Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
#9- Crear una función que reciba una lista de números y genere una nueva lista que contenga únicamente los números positivos.
#10- Crear una función que reciba una lista de productos (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.


