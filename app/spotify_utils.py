import requests
from urllib.parse import urlencode

REDIRECT_URI = "http://localhost:6969/callback"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
SCOPE = "user-read-recently-played user-top-read playlist-read-private"

def get_auth_url(client_id):
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE
    }
    return f"{AUTH_URL}?{urlencode(params)}"

def get_token(code, client_id, client_secret):
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "client_secret": client_secret
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    res = requests.post(TOKEN_URL, data=payload, headers=headers)
    return res.json()
