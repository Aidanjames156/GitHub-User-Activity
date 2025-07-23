import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("Usage: python useractivity.py <github-username>")
        return
    user = sys.argv[1]
    url = f"https://api.github.com/users/{user}/events/public"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch activity for user '{user}'. Status code: {response.status_code}")
        return
    events = response.json()
    if not events:
        print(f"No recent public activity found for user '{user}'.")
        return
    print(f"Recent public activity for {user}:")
    for event in events[:10]:  # Show up to 10 recent events
        event_type = event.get("type")
        repo = event.get("repo", {}).get("name")
        created_at = event.get("created_at")
        print(f"- [{created_at}] {event_type} in {repo}")

if __name__ == "__main__":
    main()
