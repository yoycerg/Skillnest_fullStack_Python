from flask import Flask
from config import Config
from controllers.auth_controller import auth_bp
from controllers.book_controller import books_bp
from controllers.favorite_controller import favorites_bp
from controllers.main_controller import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.context_processor
    def inject_today():
        from datetime import date
        return {"today": date.today().isoformat()}

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(favorites_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
