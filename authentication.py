from flask import request, redirect, render_template, session

# ...

@app.before_request
def require_login():
    if "user_email" not in session:
        return redirect("/login")

# Replace this dictionary with a proper user database or authentication mechanism
users = {
    "user@example.com": "password123",
    "anotheruser@example.com": "securepassword"
}

def validate_user(email, password):
    if email in users and users[email] == password:
        return True
    return False


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Validate the email and password (replace this with your authentication logic)
        if validate_user(email, password):
            # Set the user's email in the session
            session["user_email"] = email
            return redirect("/dashboard")  # Redirect to the user's dashboard page
        else:
            return "Invalid credentials. Please try again."

    return render_template("login.html")


