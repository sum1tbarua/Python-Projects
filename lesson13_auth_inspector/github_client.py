import os
import requests

BASE_URL = "https://api.github.com"

def build_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "auth-inspector-cli"
    }
    
    token = os.getenv("GITHUB_TOKEN")
    
    if token:
        print("Using token authentication")
        headers["Authorization"] = f"Bearer {token}"
    else:
        print("No token found.")
    return headers

def get_authenticated_user():
    url = f"{BASE_URL}/user"
    response = requests.get(url, headers=build_headers())
    return response