from functools import wraps

from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.user import User, GENDERS, LANGUAGES

bcrypt = Bcrypt(app)


def login_required(view):
    """Solo deja pasar a quienes tienen sesión iniciada."""
    @wraps(view)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Debes iniciar sesión para ver esa página.", "login")
            return redirect("/")
        return view(*args, **kwargs)
    return wrapper


@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/success")
    return render_template("index.html", genders=GENDERS, languages=LANGUAGES)


@app.route("/register", methods=["POST"])
def register():
    # Guardamos lo escrito (menos contraseñas) para no borrar el formulario si hay errores
    session["form"] = {
        k: request.form.get(k, "")
        for k in ("first_name", "last_name", "email", "birth_date", "gender", "favorite_language")
    }

    if not User.validate_register(request.form):
        return redirect("/")

    data = {
        "first_name": request.form["first_name"].strip(),
        "last_name": request.form["last_name"].strip(),
        "email": request.form["email"].strip(),
        "password": bcrypt.generate_password_hash(request.form["password"]),
        "birth_date": request.form["birth_date"],
        "gender": request.form["gender"],
        "favorite_language": request.form["favorite_language"],
    }
    user_id = User.save(data)
    if not user_id:
        flash("Ocurrió un error al guardar el registro.", "register")
        return redirect("/")

    session.pop("form", None)
    session["user_id"] = user_id
    return redirect("/success")


@app.route("/login", methods=["POST"])
def login():
    session.pop("form", None)
    user = User.get_by_email(request.form["email"].strip())

    # Mismo mensaje en ambos casos: no revelamos si el correo existe
    if not user:
        flash("E-mail o contraseña incorrectos.", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("E-mail o contraseña incorrectos.", "login")
        return redirect("/")

    session["user_id"] = user.id
    return redirect("/success")


@app.route("/success")
@login_required
def success():
    user = User.get_by_id(session["user_id"])
    if not user:  # el usuario ya no existe en la BD
        session.clear()
        return redirect("/")
    return render_template("success.html", user=user)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
