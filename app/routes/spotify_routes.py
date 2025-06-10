# app/routes/spotify_routes.py

from flask import Blueprint
from app.spotify_client import SpotifyClient

spotify_bp = Blueprint("spotify", __name__)

@spotify_bp.route("/me")
def me():
    client = SpotifyClient()
    return client.get_user_profile()

@spotify_bp.route("/top-tracks")
def top_tracks():
    client = SpotifyClient()
    return client.get_top_tracks()

@spotify_bp.route("/related-artists/<artist_id>")
def related_artists(artist_id):
    client = SpotifyClient()
    return client.get_related_artists(artist_id)


