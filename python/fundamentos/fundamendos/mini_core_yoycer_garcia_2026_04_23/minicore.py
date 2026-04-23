datos = [
      {"nombre": "Carlos", "puntaje": 80},
      {"nombre": "María", "puntaje": 95},
      {"nombre": "Pedro", "puntaje": 70}
]

datos[2]["puntaje"] = 75
print(datos)

def puntos(lista):
    for i in lista:
        print(f"{i['nombre']} {i['puntaje']} ")

puntos(datos)        