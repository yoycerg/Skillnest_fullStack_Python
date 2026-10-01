import re
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user_model import create_user, get_user_by_email

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate_registration(first_name, last_name, email, password, confirm_password):
    errors = []

    if len(first_name.strip()) < 2:
        errors.append("El nombre debe tener al menos 2 caracteres.")
    if len(last_name.strip()) < 2:
        errors.append("El apellido debe tener al menos 2 caracteres.")
    if not EMAIL_RE.match(email):
        errors.append("Ingresa un correo electrónico válido.")
    if len(password) < 8:
        errors.append("La contraseña debe tener al menos 8 caracteres.")
    if password != confirm_password:
        errors.append("La contraseña y su confirmación deben coincidir.")

    return errors

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Completa el correo y la contraseña.", "danger")
            return render_template("auth/login_register.html", mode="login")

        user = get_user_by_email(email)
        if not user or not bcrypt.checkpw(
            password.encode("utf-8"),
            user["password_hash"].encode("utf-8")
        ):
            flash("Correo o contraseña incorrectos.", "danger")
            return render_template("auth/login_register.html", mode="login")

        session.clear()
        session["user_id"] = user["id"]
        session["user_name"] = user["first_name"]
        flash("Inicio de sesión correcto.", "success")
        return redirect(url_for("books.index"))

    return render_template("auth/login_register.html", mode="login")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        errors = validate_registration(
            first_name, last_name, email, password, confirm_password
        )

        if get_user_by_email(email):
            errors.append("Ese correo ya está registrado.")

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template("auth/login_register.html", mode="register")

        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        create_user(first_name, last_name, email, password_hash)
        flash("Cuenta creada correctamente. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/login_register.html", mode="register")

@auth_bp.get("/logout")
def logout():
    session.clear()
    flash("Sesión cerrada.", "info")
    return redirect(url_for("auth.login"))
