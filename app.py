from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/python1")
def python1():
    return render_template("python1.html")

@app.route("/ex-python1")
def ex_python1():
    return render_template("ex-python1.html")

if __name__ == "__main__":
    app.run(debug=True)