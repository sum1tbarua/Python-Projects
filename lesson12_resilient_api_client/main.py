# main.py
from api_client import fetch_with_retry
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Resilient API Client"
    )
    parser.add_argument("--endpoint", required=True, choices=["posts", "comments", "users"])
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=5)
    
    args = parser.parse_args()
    data = fetch_with_retry(args.endpoint, args.retries, args.timeout)       
    
    if data is None:
        print("Request failed.")
    else:
        print("Request completed successfully.")
    
if __name__ == "__main__":
    main()