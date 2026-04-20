"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

def generarNiveles():
 for numero in range(1,101):
    print(numero)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

def potenciarEnergia():
  for numero in range(2, 501, 2):
     print(numero)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

def trampaEmojis():
  for numero in range(5, 101):
    if numero % 10 == 0:
        print("😂")
    elif numero % 5 == 0:
      print("🎮")
    else:
      print(numero)
# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)
def sumaColosal():
  total_suma = 0
  for numero in range(0, 500001, 2):
    total_suma += numero
    print(total_suma)

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)
def retrocesoTemporal():
    for anio in range(2024, -1 , -3):
      print(anio)



# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

def contadorDinamico(inicio, fin, salto):
  for numero in range(inicio + salto, fin + 1, salto):
    print(numero)





continuar = True
while continuar:
    print("\n --- ejercicio 1 Python---")
    print(" ---1 ejercicio 1 ---")
    print(" ---2 ejercicio 2 ---")    
    print(" ---3 ejercicio 3 ---")
    print(" ---4 ejercicio 4 ---")
    print(" ---5 ejercicio 5 ---")
    print(" ---6 ejercicio 6 ---")
    print(" ---7 ejercicio 7 ---")
    print(" ---8 ejercicio 8 ---")
    print(" ---9 ejercicio 9 ---")
    print(" ---10 ejercicio 10 ---")
    print(" ---11 ejercicio 11 ---")
    print(" ---12 ejercicio 12 ---")
    print(" ---13 ejercicio 13 ---")
    print(" ---14 ejercicio 14 ---")
    print(" ---15 ejercicio 15 ---")
    opcion = input("\n---- Elige una opción (1-15) o '(0 para salir)= ")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(generarNiveles())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        print(potenciarEnergia())
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        print(trampaEmojis())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        print(sumaColosal())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        print(retrocesoTemporal())

    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        print(contadorDinamico())
   


    elif opcion == "0":
        print("Saliendo...") 
        continuar = False
    else:
        print("Opción no válida, intenta otra vez")
                  

