# ==========================================
# IMPORTACIONES
# ==========================================

from flask import Flask, render_template, request, redirect


# ==========================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================

app = Flask(__name__)


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    """
    Muestra el formulario de registro de productos.
    """

    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/registrar", methods=["POST"])
def registrar():
    """
    Recibe la información enviada mediante POST.

    Esta función se encarga de procesar los datos
    antes de realizar la redirección.
    """

    # ------------------------------------------
    # Obtener los datos enviados por el formulario
    # ------------------------------------------

    nombre = request.form["nombre"]

    precio = request.form["precio"]

    categoria = request.form["categoria"]


    # ------------------------------------------
    # Mostrar los datos en la terminal
    # ------------------------------------------

    print("============================")

    print("Producto recibido")

    print(f"Nombre: {nombre}")

    print(f"Precio: {precio}")

    print(f"Categoría: {categoria}")

    print("============================")


    # ------------------------------------------
    # Redireccionar al usuario
    # ------------------------------------------

    return redirect("/resultado")


# ==========================================
# MOSTRAR RESULTADO
# ==========================================

@app.route("/resultado")
def resultado():
    """
    Esta ruta recibe una solicitud GET después
    de la redirección.
    """

    print("Producto redirigido")

    # ------------------------------------------
    # request.form estará vacío aquí
    # ------------------------------------------

    print(request.form)


    # ------------------------------------------
    # Mostrar la plantilla
    # ------------------------------------------

    return render_template("resultado.html")


# ==========================================
# AYUDA (Desafío adicional)
# ==========================================

@app.route("/ayuda")
def ayuda():
    """
    Explica brevemente los conceptos de GET, POST,
    redirect() y por qué request.form no persiste
    después de una redirección.
    """

    return render_template("ayuda.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)
