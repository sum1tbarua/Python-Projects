import os
import requests
from datetime import datetime
from config import *
from exceptions import *

def build_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "auth-inspector-cli"
    }
    
    if GITHUB_TOKEN:
        print("Using token authentication")
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

def get_authenticated_user():
    url = f"{BASE_URL}/user"
    response = requests.get(url, headers=build_headers())
    
    if response.status_code == 200:
        return response.json()
    if response.status_code == 401:
        raise GitHubAuthError("Authentication failed. Missing or invalid GitHub token.")
    if response.status_code == 403:
        rate_limit = extract_rate_limit_info(response)
        if rate_limit['remaining'] == '0':
            raise GitHubRateLimitError(
                f"GitHub rate limit exceeded. Reset at {rate_limit['reset']}."
            )
        raise GitHubUnexpectedError("GitHub rejected the request with status 403.")
    raise GitHubUnexpectedError(
        f"Unexpected GitHub response: {response.status_code}"
    )

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