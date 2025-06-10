# app/token_manager.py

import time

class TokenStore:
    def __init__(self, token_data):
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        self.expires_at = time.time() + token_data["expires_in"]
        self.scope = token_data.get("scope")

    def is_expired(self):
        return time.time() > self.expires_at - 60  # refresh 60s early

    def to_dict(self):
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
            "scope": self.scope
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)
        obj.access_token = data["access_token"]
        obj.refresh_token = data["refresh_token"]
        obj.expires_at = data["expires_at"]
        obj.scope = data["scope"]
        return obj
