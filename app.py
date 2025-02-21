from flask import Flask, render_template
import forms
from flask_login import login_required, login_user, logout_user

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

# @app.route("/register")
# def register():
#     return render_template("register.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()
    if not form.validate_on_submit():
        return flask.render_template(
"register.html",
form=form,
)
    user = models.User() # Initialize the user here
    form.populate_obj(user) # Populate the user object with form data
    role = models.Role.query.filter_by(name="user").first()
    if not role: # Create the 'user' role if it doesn't exist
        role = models.Role(name="user")
        models.db.session.add(role)
    user.roles.append(role)
    user.password_hash = form.password.data
    models.db.session.add(user)
    models.db.session.commit()
    return flask.redirect(flask.url_for("index"))

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