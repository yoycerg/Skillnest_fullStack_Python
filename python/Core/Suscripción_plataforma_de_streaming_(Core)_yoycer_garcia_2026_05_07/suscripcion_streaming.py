class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def pagar_suscripcion(self, monto):
        """Realiza un pago y reduce el saldo pendiente."""
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return   

        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"Pago realizado: ${monto:.2f}. Saldo pendiente: ${self.saldo_pendiente:.2f}")

    def actualizar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y ajusta el costo mensual."""
        if nuevo_tipo not in SuscripcionStreaming.costos_suscripcion:
            print("Tipo de suscripción no válido.")
            return

        self.tipo_suscripcion = nuevo_tipo
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
        self.saldo_pendiente += self.costo_mensual  # Agrega el nuevo costo al saldo pendiente

        print(f"Suscripción cambiada a {nuevo_tipo}. Nuevo costo mensual: ${self.costo_mensual:.2f}")

    def acceder_contenido_exclusivo(self):
        """Permite el acceso a contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Gratis":
            print("Acceso denegado. Actualiza tu suscripción para ver contenido exclusivo.")
        else:
            print(f"Acceso concedido. Disfruta del contenido exclusivo con tu suscripción {self.tipo_suscripcion}.")

    def mostrar_estado_suscripcion(self):
        """Muestra el estado actual de la suscripción del usuario."""
        print(f"Usuario: {self.usuario}")
        print(f"Tipo de Suscripción: {self.tipo_suscripcion}")
        print(f"Costo Mensual: ${self.costo_mensual:.2f}")
        print(f"Saldo Pendiente: ${self.saldo_pendiente:.2f}")


# Pruebas
if __name__ == "__main__":

    # Crear usuarios con diferentes tipos de suscripción
    usuario1 = SuscripcionStreaming("Alice", "Gratis")
    usuario2 = SuscripcionStreaming("Bob", "Estándar")
    usuario3 = SuscripcionStreaming("Charlie", "Premium")

    # Usuario 1 intenta ver contenido exclusivo, mejora su suscripción y paga su saldo
    print("Usuario 1:")
    usuario1.acceder_contenido_exclusivo()
    usuario1.actualizar_suscripcion("Estándar")
    usuario1.pagar_suscripcion(5.99)
    usuario1.mostrar_estado_suscripcion()

    # Usuario 2 ve contenido exclusivo, cambia a Premium y paga dos veces
    print("\nUsuario 2:")
    usuario2.acceder_contenido_exclusivo()
    usuario2.actualizar_suscripcion("Premium")
    usuario2.pagar_suscripcion(10.99)
    usuario2.pagar_suscripcion(10.99)
    usuario2.mostrar_estado_suscripcion()

    # Usuario 3 intenta pagar una cantidad menor a su saldo pendiente y ve contenido exclusivo
    print("\nUsuario 3:")
    usuario3.pagar_suscripcion(5)  # Pago insuficiente
    usuario3.acceder_contenido_exclusivo()
    usuario3.mostrar_estado_suscripcion()