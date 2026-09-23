# ==========================================================
# CONTROLADOR: PERSONAS
# (rutas bajo /usuarios, según la consigna)
# ==========================================================

from flask import render_template, request, redirect, url_for

from flask_app import app
from flask_app.models.persona import Persona


def _leer_formulario():
    """
    Extrae y limpia los campos del formulario de persona.
    """

    return {
        "nombre": request.form.get("campo_nombre", "").strip(),
        "apellido": request.form.get("campo_apellido", "").strip(),
        "email": request.form.get("campo_email", "").strip(),
    }


def _formulario_valido(datos):
    return bool(datos["nombre"] and datos["apellido"] and datos["email"])


# ==========================================================
# READ - listado
# ==========================================================

@app.route("/usuarios")
def listado():
    personas = Persona.obtener_todos()

    return render_template(
        "listado.html",
        personas=personas
    )


# ==========================================================
# CREATE - formulario
# ==========================================================

@app.route("/usuarios/nuevo")
def formulario_nuevo():
    return render_template("formulario_nuevo.html")


# ==========================================================
# CREATE - procesar
# ==========================================================

@app.route("/usuarios/crear", methods=["POST"])
def crear_persona():
    datos = _leer_formulario()

    if not _formulario_valido(datos):
        return render_template(
            "formulario_nuevo.html",
            error="Todos los campos son obligatorios.",
            valores=datos
        )

    resultado = Persona.crear(datos)

    if resultado is False:
        return render_template(
            "formulario_nuevo.html",
            error="No fue posible crear el registro.",
            valores=datos
        )

    return redirect(url_for("listado"))


# ==========================================================
# READ - detalle
# ==========================================================

@app.route("/usuarios/<int:id_persona>")
def ver_persona(id_persona):
    persona = Persona.obtener_por_id(id_persona)

    if persona is None:
        return "Registro no encontrado", 404

    return render_template(
        "detalle_persona.html",
        persona=persona
    )


# ==========================================================
# UPDATE - formulario
# ==========================================================

@app.route("/usuarios/editar/<int:id_persona>")
def formulario_editar(id_persona):
    persona = Persona.obtener_por_id(id_persona)

    if persona is None:
        return "Registro no encontrado", 404

    return render_template(
        "formulario_editar.html",
        persona=persona
    )


# ==========================================================
# UPDATE - procesar
# ==========================================================

@app.route("/usuarios/<int:id_persona>/actualizar", methods=["POST"])
def actualizar_persona(id_persona):
    datos = _leer_formulario()
    datos["id"] = id_persona

    if not _formulario_valido(datos):
        persona = Persona.obtener_por_id(id_persona)

        return render_template(
            "formulario_editar.html",
            persona=persona,
            error="Todos los campos son obligatorios."
        )

    resultado = Persona.actualizar(datos)

    if resultado is False:
        persona = Persona.obtener_por_id(id_persona)

        return render_template(
            "formulario_editar.html",
            persona=persona,
            error="No fue posible actualizar el registro."
        )

    return redirect(url_for("listado"))


# ==========================================================
# DELETE
# ==========================================================

@app.route("/usuarios/borrar/<int:id_persona>")
def eliminar_persona(id_persona):
    resultado = Persona.eliminar(id_persona)

    if resultado is False:
        return "No fue posible eliminar el registro.", 500

    return redirect(url_for("listado"))
