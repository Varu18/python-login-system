from flask import Flask, render_template, request, flash, session
from dotenv import load_dotenv
import os
from database import init_db, create_user, check_user

load_dotenv()

app = Flask(__name__)

app.secret_key = "SECRET_KEY"

init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_user(username, password):
            session["username"] = username
            return "Logged in!"

        flash("Invalid username or password.")
        
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if len(password) < 8:
            flash("Password must contain at least 8 characters.")
            return render_template("signup.html")

        if not any(char.isalpha() for char in password):
            flash("Password must contain at least one letter.")
            return render_template("signup.html")

        if not any(char.isdigit() for char in password):
            flash("Password must contain at least one number.")
            return render_template("signup.html")

        if create_user(username, password):
            flash("Account created successfully!")
        else:
            flash("Username already exists.")

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)