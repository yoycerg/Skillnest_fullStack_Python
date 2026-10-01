from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.decorators import login_required
from models.book_model import (
    get_all_books, get_book_by_id, get_genres,
    create_book, update_book, delete_book
)
from models.favorite_model import (
    is_favorite, get_book_favorite_users
)

books_bp = Blueprint("books", __name__, url_prefix="/libros")

def validate_book_form(title, author, genre_id, publication_date, description):
    errors = []

    if len(title.strip()) < 2:
        errors.append("El título debe tener al menos 2 caracteres.")
    if len(author.strip()) < 2:
        errors.append("El autor debe tener al menos 2 caracteres.")
    if not genre_id:
        errors.append("Debes seleccionar un género.")
    if not publication_date:
        errors.append("La fecha de publicación es obligatoria.")
    else:
        try:
            pub_date = date.fromisoformat(publication_date)
            if pub_date > date.today():
                errors.append("La fecha de publicación no puede ser futura.")
        except ValueError:
            errors.append("La fecha de publicación no es válida.")

    if len(description.strip()) < 10:
        errors.append("La descripción debe tener al menos 10 caracteres.")

    return errors

@books_bp.get("")
@login_required
def index():
    books = get_all_books()
    user_books = [book for book in books if book["user_id"] == session["user_id"]]
    community_books = [book for book in books if book["user_id"] != session["user_id"]]
    return render_template(
        "books/index.html",
        user_books=user_books,
        community_books=community_books
    )

@books_bp.route("/nuevo", methods=["GET", "POST"])
@login_required
def new_book():
    genres = get_genres()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        genre_id = request.form.get("genre_id", "")
        publication_date = request.form.get("publication_date", "")
        description = request.form.get("description", "").strip()

        errors = validate_book_form(
            title, author, genre_id, publication_date, description
        )

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template("books/new.html", genres=genres)

        create_book(
            title, author, int(genre_id), publication_date,
            description, session["user_id"]
        )
        flash("Libro creado correctamente.", "success")
        return redirect(url_for("books.index"))

    return render_template("books/new.html", genres=genres)

@books_bp.route("/editar/<int:book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = get_book_by_id(book_id)

    if not book:
        flash("El libro no existe.", "danger")
        return redirect(url_for("books.index"))

    if book["user_id"] != session["user_id"]:
        flash("No puedes editar un libro que no te pertenece.", "danger")
        return redirect(url_for("books.index"))

    genres = get_genres()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        genre_id = request.form.get("genre_id", "")
        publication_date = request.form.get("publication_date", "")
        description = request.form.get("description", "").strip()

        errors = validate_book_form(
            title, author, genre_id, publication_date, description
        )

        if errors:
            for error in errors:
                flash(error, "danger")
            book.update({
                "title": title,
                "author": author,
                "genre_id": int(genre_id) if genre_id.isdigit() else None,
                "publication_date": publication_date,
                "description": description,
            })
            return render_template("books/edit.html", book=book, genres=genres)

        update_book(
            book_id, title, author, int(genre_id), publication_date,
            description, session["user_id"]
        )
        flash("Libro actualizado correctamente.", "success")
        return redirect(url_for("books.index"))

    return render_template("books/edit.html", book=book, genres=genres)

@books_bp.post("/eliminar/<int:book_id>")
@login_required
def delete(book_id):
    book = get_book_by_id(book_id)

    if not book:
        flash("El libro no existe.", "danger")
    elif book["user_id"] != session["user_id"]:
        flash("No puedes eliminar un libro que no te pertenece.", "danger")
    elif delete_book(book_id, session["user_id"]):
        flash("Libro eliminado correctamente.", "success")
    else:
        flash("No se pudo eliminar el libro.", "danger")

    return redirect(url_for("books.index"))

@books_bp.get("/<int:book_id>")
@login_required
def detail(book_id):
    book = get_book_by_id(book_id)

    if not book:
        flash("El libro no existe.", "danger")
        return redirect(url_for("books.index"))

    favorite = is_favorite(session["user_id"], book_id)
    favorite_users = get_book_favorite_users(book_id)

    return render_template(
        "books/detail.html",
        book=book,
        favorite=favorite,
        favorite_users=favorite_users
    )
