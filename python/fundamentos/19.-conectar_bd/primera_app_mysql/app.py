# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================


from flask import Flask, render_template

from mascota import Mascota


# ==========================================================
# CREAR APLICACIÓN
# ==========================================================

app = Flask(__name__)


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Consulta todas las mascotas de la base de datos
    y las envía hacia la plantilla HTML.
    """

    # ------------------------------------------------------
    # Consultar base de datos mediante el modelo.
    # ------------------------------------------------------

    mascotas = Mascota.get_all()


    # ------------------------------------------------------
    # Mostrar resultados en la terminal.
    # ------------------------------------------------------

    mascota = Mascota.get_by_id(3)

    print(mascota)
    print(mascota.nombre)
    print(mascota.tipo)
    print(mascota.color)

    return "Revisa la terminal"




    # ------------------------------------------------------
    # Enviar resultados a Jinja2.
    # ------------------------------------------------------

    return render_template(
        "index.html",
        mascotas=mascotas
    )


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(debug=True)
