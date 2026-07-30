from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "icono": "fa-spotify", "color": "#1DB954"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "icono": "netflix", "color": "#E50914"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "icono": "fa-youtube", "color": "#FF0000"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "icono": "fa-twitch", "color": "#9146FF"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "icono": "fa-tiktok", "color": "#000000"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "icono": "fa-instagram", "color": "#E1306C"},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "icono": "fa-discord", "color": "#5865F2"},
]


# Ruta para mostrar la tabla con datos
@app.route("/tabla")
def tabla():
    # Ordenamos por nombre de forma ascendente para la carga inicial
    datos_ordenados = sorted(datos, key=lambda d: d["nombre"])
    # Lista de países únicos para el filtro (ordenada alfabéticamente)
    paises = sorted(set(d["pais"] for d in datos))
    return render_template("tabla.html", datos=datos_ordenados, paises=paises)


@app.route("/")
def index():
    return tabla()


if __name__ == "__main__":
    app.run(debug=True)
