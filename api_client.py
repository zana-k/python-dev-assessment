import requests


def fetch_and_display_users(num_users):
    """Fetches user data from JSONPlaceholder API and displays name, email, and city for the specified number of users. Handles errors."""

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        users = response.json()

        print(f"\n--- Fetching and Displaying {num_users} Users ---")

        target_users = users[:num_users]

        for index, user in enumerate(target_users, 1):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"User {index}:")
                print(f"  Name:  {name}")
                print(f"  Email: {email}")
                print(f"  City:  {city}\n")

            except KeyError as ke:
                print(f"[Data Error]: Expected user key missing from JSON response: {ke}")

    except requests.exceptions.RequestException as re:
        print(f"\n[API Error]: Failed to connect or retrieve data from API. Details: {re}")
        return None

if __name__ == "__main__":
    fetch_and_display_users(4)
    fetch_and_display_users(16)