from flask import Flask, render_template

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
    return render_template("learn/python1.html")

@app.route("/python2")
def python2():
    return render_template("learn/python2.html")

@app.route("/python3")
def python3():
    return render_template("learn/python3.html")

@app.route("/python4")
def python4():
    return render_template("learn/python4.html")

@app.route("/python5")
def python5():
    return render_template("learn/python5.html")

@app.route("/python6")
def python6():
    return render_template("learn/python6.html")


if __name__ == "__main__":
    app.run(debug=True)