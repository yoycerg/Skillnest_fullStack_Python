from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# ---------------------------------------------------------
# Datos usados para generar la "predicción" del destino
# ---------------------------------------------------------

# Mensajes de destino: unos positivos y otros de mala suerte
MENSAJES_POSITIVOS = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Una gran oportunidad laboral está a punto de tocar tu puerta. Prepárate para aprovecharla.",
    "Tus esfuerzos darán frutos muy pronto. La abundancia se acerca a tu vida.",
    "Un viaje inesperado traerá aventuras y aprendizajes que recordarás para siempre.",
    "Recibirás buenas noticias de una persona que hace tiempo no ves.",
]

MENSAJES_NEGATIVOS = [
    "Debes tener cuidado con las decisiones financieras en las próximas semanas.",
    "Una amistad pondrá a prueba tu paciencia, pero saldrás fortalecido.",
    "Se avecina un periodo de cambios inesperados; mantén la calma y la mente clara.",
    "Podrías enfrentar un pequeño obstáculo, pero tu perseverancia lo superará.",
    "Alguien cercano podría decepcionarte, confía en tu propio criterio.",
]

# Significado según el color favorito
SIGNIFICADO_COLORES = {
    "rojo": "pasión y energía",
    "azul": "calma y sabiduría",
    "verde": "misterio y descubrimiento",
    "amarillo": "alegría y creatividad",
    "morado": "intuición y espiritualidad",
    "naranja": "entusiasmo y aventura",
    "negro": "poder y elegancia",
    "blanco": "pureza y nuevos comienzos",
    "rosa": "ternura y compasión",
    "gris": "equilibrio y neutralidad",
}

# Significado según el animal favorito
SIGNIFICADO_ANIMALES = {
    "gato": "independencia y misterio",
    "perro": "lealtad y protección",
    "águila": "visión y libertad",
    "leon": "coraje y liderazgo",
    "león": "coraje y liderazgo",
    "delfín": "inteligencia e intuición",
    "lobo": "instinto y comunidad",
    "búho": "sabiduría y conocimiento oculto",
    "tigre": "fuerza y determinación",
    "mariposa": "transformación y renovación",
}

# Colores hexadecimales usados para pintar el círculo de "Tu Color"
COLORES_HEX = {
    "rojo": "#dc2626",
    "azul": "#2563eb",
    "verde": "#16a34a",
    "amarillo": "#eab308",
    "morado": "#9333ea",
    "naranja": "#f97316",
    "negro": "#111827",
    "blanco": "#f9fafb",
    "rosa": "#ec4899",
    "gris": "#6b7280",
}


# ---------------------------------------------------------
# Rutas
# ---------------------------------------------------------

@app.route("/")
def index():
    """Muestra el formulario para ingresar los datos del usuario."""
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    """Recibe los datos del formulario, los guarda en sesión y redirige a /futuro."""
    session["nombre"] = request.form.get("nombre", "").strip() or "Viajero"
    session["edad"] = request.form.get("edad", "").strip() or "?"
    session["color"] = request.form.get("color", "").strip().lower() or "morado"
    session["animal"] = request.form.get("animal", "").strip().lower() or "gato"
    return redirect("/futuro")


@app.route("/futuro")
def futuro():
    """Muestra la predicción del destino generada a partir de los datos en sesión."""
    # Si el usuario entra directo a /futuro sin pasar por el formulario
    if "nombre" not in session:
        return redirect("/")

    nombre = session.get("nombre")
    edad = session.get("edad")
    color = session.get("color")
    animal = session.get("animal")

    # Elegimos aleatoriamente si el mensaje es positivo o negativo
    es_positivo = random.choice([True, False])
    mensaje = random.choice(MENSAJES_POSITIVOS if es_positivo else MENSAJES_NEGATIVOS)

    significado_color = SIGNIFICADO_COLORES.get(color, "originalidad y sorpresa")
    significado_animal = SIGNIFICADO_ANIMALES.get(animal, "curiosidad y aventura")
    color_hex = COLORES_HEX.get(color, "#7c3aed")

    numero_suerte = random.randint(1, 99)

    return render_template(
        "futuro.html",
        nombre=nombre,
        edad=edad,
        color=color,
        animal=animal,
        significado_color=significado_color,
        significado_animal=significado_animal,
        color_hex=color_hex,
        numero_suerte=numero_suerte,
        mensaje=mensaje,
        es_positivo=es_positivo,
    )


if __name__ == "__main__":
    app.run(debug=True)
