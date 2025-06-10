# app/spotify_client.py

import requests
from app.auth import get_valid_token

class SpotifyClient:
    def __init__(self):
        self.token = get_valid_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get(self, endpoint, params=None):
        url = f"https://api.spotify.com/v1/{endpoint}"
        return requests.get(url, headers=self.headers, params=params).json()

    def put(self, endpoint, data=None):
        url = f"https://api.spotify.com/v1/{endpoint}"
        return requests.put(url, headers=self.headers, json=data).json()

    def post(self, endpoint, data=None):
        url = f"https://api.spotify.com/v1/{endpoint}"
        return requests.post(url, headers=self.headers, json=data).json()

    # Optional: Add custom helper methods
    def get_related_artists(self, artist_id):
        return self.get(f"artists/{artist_id}/related-artists")
