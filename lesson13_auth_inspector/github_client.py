import os
import requests
from datetime import datetime
from config import *

def build_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "auth-inspector-cli"
    }
    
    if GITHUB_TOKEN:
        print("Using token authentication")
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    else:
        print("No token found.")
    return headers

def get_authenticated_user():
    url = f"{BASE_URL}/user"
    response = requests.get(url, headers=build_headers())
    return response

def extract_rate_limit_info(response):
    limit = response.headers.get("X-RateLimit-Limit")
    remaining = response.headers.get("X-RateLimit-Remaining")
    reset = response.headers.get("X-RateLimit-Reset")
    
    reset_readable = "unknown"
    
    if reset and str(reset).isdigit():
        reset_readable = datetime.fromtimestamp(int(reset)).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "limit": limit,
        "remaining": remaining,
        "reset": reset_readable
    }