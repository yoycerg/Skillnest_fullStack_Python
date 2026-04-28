#🧪 Realizar las siguientes pruebas con instancias:

#Crea 3 usuarios de la plataforma de streaming.
#Haz que el primer usuario agregue dos títulos a su lista y los vea.
#Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
#Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.

class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)
       print(f"Titulo '{titulo}'agregado correctamente. ")
      


   def ver_contenido(self, titulo):
       """Simula que el usuario reproduce un contenido."""
       for titulo in self.lista_reproduccion:
           print(f"El usuario {self.nombre} esta viendo {titulo}")
      


   def cambiar_suscripcion(self, nueva_suscripcion):
       """Cambia el tipo de suscripción del usuario."""
       susAntigua = self.suscripcion
       self.suscripcion = nueva_suscripcion
       print(f"Suscripción cambió de {susAntigua} a {nueva_suscripcion}")
     


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripción : {self.suscripcion}")
       if len(self.lista_reproduccion) == 0:
           print("La lista de reproducción está vacia. ")
       else:
           print(f"Lista de reporducción: \n- {"\n.".join(self.lista_reproduccion)}")    

usuario_1 = UsuarioStreaming("Usuario 1", "usuario1@gmail.com")
usuario_1.agregar_a_lista("La casa de papel")
usuario_1.cambiar_suscripcion("premium")
usuario_1.ver_contenido("La casa de papel")
usuario_1.mostrar_info_usuario()



usuario_2 = UsuarioStreaming("Usuario 2", "usuario2@gmail.com")
usuario_2.agregar_a_lista("shrek")
usuario_2.cambiar_suscripcion("standar")
usuario_2.c

usuario_3 = UsuarioStreaming("Usuario 2", "usuario3@gmail.com")






