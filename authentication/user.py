from data.user import fetch_user

def validate_user(email, password):
    users = fetch_user()

    for user in users:
        if user['email'] == email and user['password'] == password:
            return True

    return False