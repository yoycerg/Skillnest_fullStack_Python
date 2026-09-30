import re
from datetime import date, datetime

from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

DB = "login_registro_db"
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
LETTERS_REGEX = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+$")

GENDERS = ["Femenino", "Masculino", "Otro", "Prefiero no decirlo"]
LANGUAGES = ["Python", "JavaScript", "Java", "C#"]


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.birth_date = data["birth_date"]
        self.gender = data["gender"]
        self.favorite_language = data["favorite_language"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ---------- Consultas ----------
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password, birth_date, gender, favorite_language)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(birth_date)s, %(gender)s, %(favorite_language)s);
        """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, {"email": email})
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, {"id": user_id})
        if not results:
            return False
        return cls(results[0])

    # ---------- Validaciones ----------
    @staticmethod
    def validate_register(data):
        is_valid = True

        # Nombre
        name = data["first_name"].strip()
        if not name:
            flash("El nombre no puede estar vacío.", "register")
            is_valid = False
        elif len(name) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not LETTERS_REGEX.match(name):
            flash("El nombre solo puede contener letras.", "register")
            is_valid = False

        # Apellido
        last = data["last_name"].strip()
        if not last:
            flash("El apellido no puede estar vacío.", "register")
            is_valid = False
        elif len(last) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not LETTERS_REGEX.match(last):
            flash("El apellido solo puede contener letras.", "register")
            is_valid = False

        # Email
        email = data["email"].strip()
        if not email:
            flash("El e-mail no puede estar vacío.", "register")
            is_valid = False
        elif not EMAIL_REGEX.match(email):
            flash("El formato del e-mail no es válido.", "register")
            is_valid = False
        elif User.get_by_email(email):
            flash("Ese e-mail ya está registrado.", "register")
            is_valid = False

        # Contraseña
        password = data["password"]
        if not password:
            flash("La contraseña no puede estar vacía.", "register")
            is_valid = False
        else:
            if len(password) < 8:
                flash("La contraseña debe tener al menos 8 caracteres.", "register")
                is_valid = False
            # BONUS DE PLATA: al menos un número y una mayúscula
            if not re.search(r"\d", password):
                flash("La contraseña debe incluir al menos un número.", "register")
                is_valid = False
            if not re.search(r"[A-Z]", password):
                flash("La contraseña debe incluir al menos una letra mayúscula.", "register")
                is_valid = False

        # Confirmación
        if data["confirm_password"] != password:
            flash("La confirmación no coincide con la contraseña.", "register")
            is_valid = False

        # BONUS DE ORO: fecha de nacimiento (solo mayores de edad)
        birth = data.get("birth_date", "")
        if not birth:
            flash("La fecha de nacimiento es obligatoria.", "register")
            is_valid = False
        else:
            try:
                born = datetime.strptime(birth, "%Y-%m-%d").date()
                today = date.today()
                age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                if born > today:
                    flash("La fecha de nacimiento no puede ser futura.", "register")
                    is_valid = False
                elif age < 18:
                    flash("Debes ser mayor de edad (18+) para registrarte.", "register")
                    is_valid = False
            except ValueError:
                flash("La fecha de nacimiento no es válida.", "register")
                is_valid = False

        # BONUS: select (género)
        if data.get("gender") not in GENDERS:
            flash("Selecciona una opción de género válida.", "register")
            is_valid = False

        # BONUS: radio (lenguaje favorito)
        if data.get("favorite_language") not in LANGUAGES:
            flash("Selecciona tu lenguaje favorito.", "register")
            is_valid = False

        # BONUS: checkbox (términos)
        if not data.get("terms"):
            flash("Debes aceptar los términos y condiciones.", "register")
            is_valid = False

        return is_valid
