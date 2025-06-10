# app/auth.py

import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import time
from flask import session
from app.token_manager import TokenStore


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

SCOPES = "user-read-private user-read-email user-top-read user-modify-playback-state user-read-playback-state streaming"

def get_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "show_dialog": "true",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES
    }
    return "https://accounts.spotify.com/authorize?" + urlencode(params)

def get_token(code):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=data)
    return response.json()


def refresh_token(refresh_token):
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=data)
    return response.json()


def get_valid_token():
    if "token" not in session:
        raise Exception("No token found in session. User must authenticate.")

    token = TokenStore.from_dict(session["token"])

    if token.is_expired():
        if not token.refresh_token:
            raise Exception("Cannot refresh access token — no refresh_token available.")
        
        refreshed_data = refresh_token(token.refresh_token)
        token = TokenStore(refreshed_data)
        session["token"] = token.to_dict()  # Update session with new tokens

    return token.access_token