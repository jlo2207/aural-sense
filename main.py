# main.py

from flask import Flask, request
from app.spotify_client import SpotifyClient

app = Flask(__name__)
app.secret_key = "some-secret"

@app.route("/me")
def me():
    client = SpotifyClient()
    return client.get_user_profile()

@app.route("/top-tracks")
def top_tracks():
    client = SpotifyClient()
    return client.get_top_tracks()

@app.route("/related-artists/<artist_id>")
def related_artists(artist_id):
    client = SpotifyClient()
    return client.get_related_artists(artist_id)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
