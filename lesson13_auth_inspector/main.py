from github_client import get_authenticated_user, extract_rate_limit_info
from exceptions import *

def main():
    print("Checking authentication...\n")
    
    try:
        user_data = get_authenticated_user()
        print("✅ Authenticated")
        print(f"Username: {user_data.get('login')}")
        
    except GitHubAuthError as e:
        print(f"❌ {e}")

    except GitHubRateLimitError as e:
        print(f"⏳ {e}")

    except GitHubUnexpectedError as e:
        print(f"⚠️ {e}")   
    

if __name__ == "__main__":
    main()