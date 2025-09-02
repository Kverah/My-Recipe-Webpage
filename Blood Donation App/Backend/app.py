# Backend/app.py

from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
import config


def create_app():
    app = Flask(
        __name__,
        static_folder="../frontend",
        template_folder="../frontend"
    )

    # Allow frontend <-> backend communication
    CORS(app)

    # Configure DB
    app.config.from_object(config)
    db.init_app(app)

    # Register blueprints (routes)
    from routes import main
    app.register_blueprint(main, url_prefix="/api")

    # Serve frontend index
    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    # Serve static files (JS, CSS, images)
    @app.route("/<path:filename>")
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # ✅ create tables if not exist
    app.run(debug=True)
