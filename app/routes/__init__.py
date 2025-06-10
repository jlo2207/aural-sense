# app/routes/__init__.py

from .spotify_routes import spotify_bp

def register_blueprints(app):
    app.register_blueprint(spotify_bp)
