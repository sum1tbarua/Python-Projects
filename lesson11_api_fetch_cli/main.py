import requests, argparse

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_data(endpoint, params=None):
    """
    Builds the full URL and fetches data from API.
    """
    try:
        full_url = f"{BASE_URL}/{endpoint}"
        response = requests.get(full_url, params=params, timeout=5)
        
        if response.status_code != 200:
            if response.status_code == 404:
                print("Error: Invalid endpoint or resource not found")
            else:
                print(f"Error: Received status code {response.status_code}")
                return None
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to API")
        return None
    except requests.exceptions.RequestException:
        print("Error: Request failed")
        return None

def format_output(endpoint, data, limit):
    """
    Check if data exists, loop through first limit items,
    and print fields depending on endpoint.
    """

    if not data:
        print("No data found")
        return
    for item in data[:limit]:
        if endpoint == "posts":
            print(f"ID: {item.get('id')}")
            print(f"User: {item.get('userId')}")
            print(f"Title: {item.get('title')}")
        elif endpoint == "comments":
            print(f"ID: {item.get('id')}")
            print(f"Email: {item.get('email')}")
            print(f"Body: {item.get('body')}")
        elif endpoint == "users":
            print(f"ID: {item.get('id')}")
            print(f"Name: {item.get('name')}")
            print(f"Username: {item.get('username')}")
        print("-" * 20)
    
        
def main():
    parser = argparse.ArgumentParser(
        description="API Fetch CLI"
    )
    parser.add_argument("--endpoint", required=True, choices=['posts', 'comments', 'users'])
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--user", type=int)
    args = parser.parse_args()
    
    params = {}
    if args.user and args.endpoint in ["posts", "comments"]:
        params['userId'] = args.user
    
    data = fetch_data(args.endpoint, params)
    format_output(args.endpoint, data, args.limit)
    

if __name__ == "__main__":
    main()