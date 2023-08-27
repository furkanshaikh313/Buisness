from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# Replace this dictionary with a proper user database or authentication mechanism
users = {
    "user@example.com": "password123",
    "anotheruser@example.com": "securepassword"
}

def validate_user(email, password):
    if email in users and users[email] == password:
        return True
    return False

@app.route("/")
def index():
    if "user_email" in session:
        return redirect("/dashboard")  # Redirect to dashboard if user is already authenticated

    return redirect("/login")  # Redirect to login if user is not authenticated

@app.route("/dashboard")
def dashboard():
    if "user_email" not in session:
        return redirect("/login")  # Redirect to login if user is not authenticated

    return render_template("dashboard.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_email" in session:
        return redirect("/dashboard")  # Redirect to dashboard if user is already authenticated

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if validate_user(email, password):
            session["user_email"] = email
            return redirect("/dashboard")  # Redirect to the user's dashboard page
        else:
            return "Invalid credentials. Please try again."

    return render_template("login.html")

if __name__ == "__main__":
    app.debug = True  # Enable debugging
    app.run()
