#Direccioner en python
estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
#Imprime el nombre del estudiante
print(estudiante["nombre"]) #Imprime: Gonzalo

#Diccionario de países
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"
print(paises) 

estudiante["nombre"] = "Yoycer"
print(estudiante["nombre"]) #Imprime: Vicente

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
   print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
   paises["CRI"] = "Costa Rica"
