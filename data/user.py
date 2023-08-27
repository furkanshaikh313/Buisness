import json 
import random
import requests

base_url = "https://backendbuisness.meetsonawane.repl.co"  # Replace with your actual Flask app's URL

def create_user(email, passw):
    user_data = {
        "email":email,
        "password": passw
    }

    # Send a POST request to create a user
    response = requests.post(f"{base_url}/create_users", json=user_data)

    # Check if the request was successful
    if response.status_code == 200:
        print("User created successfully")
    else:
        print("Error:", response.text)
       
def fetch_user():
    response = requests.get(f"{base_url}/fetch_users")

    if response.status_code == 200:
        users = response.json()
        return users
    
    else:
        print("Error:", response.text)
