# api_client.py
import requests
import time

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_with_retry(endpoint, retries=3, timeout=5):
    """
    Fetch data with retry and exponential backoff.

    Args:
        endpoint: API resource name
        retries: maximum number of attempts
        timeout: request timeout in seconds

    Returns:
        Parsed JSON data (list) or None
    """
    
    url = f"{BASE_URL}/{endpoint}"
    for attempt in range(retries):
        attempt_number = attempt + 1
        print(f"Attempt {attempt_number}: Requesting {endpoint}...")
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                try:
                    data = response.json()
                except ValueError:
                    print("Invalid JSON response")
                    return None
                if not isinstance(data, list):
                    return None
                print(f"Success on attempt {attempt_number}")
                print(f"Fetched {len(data)} records")
                return data
            elif response.status_code >= 500:
                print(f"Server error: {response.status_code}. Retrying in {2 ** attempt} seconds...")
            else:
                print(f"Attempt {attempt_number}: Permanent error {response.status_code}")
                print("Stopping retries.")
                return None
        except requests.exceptions.Timeout:
            print(f"Timeout error. Retrying in {2 ** attempt} second(s)...")
        except requests.exceptions.ConnectionError:
            print(f"Connection error. Retrying in {2 ** attempt} seconds...")
        if attempt < retries - 1:
            time.sleep(2 ** attempt)
    print("Max retries reached.")
    return None