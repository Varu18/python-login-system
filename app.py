from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = "SECRET_KEY"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print(username)
        print(password)

        flash("Account created succesfully!")
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)