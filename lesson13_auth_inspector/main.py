from github_client import get_authenticated_user

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

if __name__ == "__main__":
    main()