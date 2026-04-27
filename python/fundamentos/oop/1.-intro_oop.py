#Creación de la clase usurio - Entidad
class Usuario: 
    def __init__(self): #Constructor
       self.nombre = "Nariyoshi"
       self.apellido = "Miyagi"
       self.email = "miyagi@codingdojo.la"
       self.limite_credito = 30000
       self.saldo_pagar = 0

#Unstancias de una clase
miyagi = Usuario()
daniel = Usuario()
yoycer = Usuario()


#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "Daniel@gmail.com"
daniel.limite_credito = "100000"
daniel.saldo_pagar = "30000"
print(daniel.nombre) #Imprime: Daniel

#Valores nueva instancia
yoycer.nombre = "Yoycer"
yoycer.apellido = "Garcia"
yoycer.email = "yoycer@gmail.com"
yoycer.limite_credito = 100000 
yoycer.saldo_pagar = 5000



