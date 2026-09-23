# ==========================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ==========================================================

from flask_app import app

# Se importa para registrar las rutas del controlador.
from flask_app.controllers import personas  # noqa: F401


if __name__ == "__main__":
    app.run(debug=True)
