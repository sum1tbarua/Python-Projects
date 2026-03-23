from github_client import get_authenticated_user, extract_rate_limit_info

def main():
    print("Checking authentication...\n")
    
    response = get_authenticated_user()
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Authenticated")
        print(f"Username: {data.get('login')}")
    elif response.status_code == 401:
        print("❌ Not authenticated (missing/invalid token)")
    else:
        print(f"⚠️ Unexpected response: {response.status_code}")
        print(response.text)
    
    rate_info = extract_rate_limit_info(response)
    print("\nRate Limit Info:")
    print(f"Limit: {rate_info['limit']}")
    print(f"Remaining: {rate_info['remaining']}")
    print(f"Reset: {rate_info['reset']}")
    

if __name__ == "__main__":
    main()