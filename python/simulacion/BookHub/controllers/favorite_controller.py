from flask import Blueprint, render_template, redirect, url_for, session, flash
from utils.decorators import login_required
from models.favorite_model import (
    add_favorite, remove_favorite, get_user_favorites
)
from models.book_model import get_book_by_id

favorites_bp = Blueprint("favorites", __name__)

@favorites_bp.post("/libros/<int:book_id>/favorito")
@login_required
def toggle_favorite(book_id):
    book = get_book_by_id(book_id)

    if not book:
        flash("El libro no existe.", "danger")
        return redirect(url_for("books.index"))

    from models.favorite_model import is_favorite

    if is_favorite(session["user_id"], book_id):
        remove_favorite(session["user_id"], book_id)
        flash("Libro eliminado de favoritos.", "info")
    else:
        add_favorite(session["user_id"], book_id)
        flash("Libro agregado a favoritos.", "success")

    return redirect(url_for("books.detail", book_id=book_id))

@favorites_bp.get("/favoritos")
@login_required
def favorites():
    books = get_user_favorites(session["user_id"])
    return render_template("books/favorites.html", books=books)
