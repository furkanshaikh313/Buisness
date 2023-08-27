import requests

# Define the base URL for your Flask app
base_url = "https://backendbuisness.meetsonawane.repl.co"  # Replace with your actual Flask app's URL

# Example data for creating a user
user_data = {
    "email": "newusssser@example.com",
    "password": "newpasswosssrd"
}

# Send a POST request to create a user
response = requests.post(f"{base_url}/create_users", json=user_data)

# Check if the request was successful
if response.status_code == 200:
    print("User created successfully")
else:
    print("Error:", response.text)

# Send a GET request to fetch users
response = requests.get(f"{base_url}/fetch_users")

# Check if the request was successful
if response.status_code == 200:
    users = response.json()
    print(users)
  
else:
    print("Error:", response.text)
