from flask import Blueprint, render_template, session, redirect, url_for

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def home():
    if "user_id" in session:
        return redirect(url_for("books.index"))
    return redirect(url_for("auth.login"))
