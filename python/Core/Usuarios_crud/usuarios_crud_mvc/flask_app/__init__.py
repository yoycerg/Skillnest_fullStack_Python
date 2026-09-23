# ==========================================================
# INICIALIZACIÓN DE LA APLICACIÓN FLASK
# ==========================================================

from flask import Flask

app = Flask(__name__)

# Clave necesaria para session/flash. En producción debería
# obtenerse desde una variable de entorno, no quedar en el código.
app.secret_key = "s3cr3t0-app-personas"
