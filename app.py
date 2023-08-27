from flask import Flask, render_template, request, redirect, session
from data.user import fetch_user, create_user
from authentication.user import validate_user

app = Flask(__name__)
app.secret_key = "testv1"

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

@app.route("/register", methods=["GET", "POST"])
def register():    
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        create_user(email=email, passw=password)
        if validate_user(email, password):
            session["user_email"] = email
            return redirect("/dashboard")  # Redirect to the user's dashboard page
        
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True  # Enable debugging
    app.run()
