import flask
import models
import forms
# from models import db, User, Tag
from flask_login import login_required, login_user, logout_user
from flask import Response, send_file, abort ,render_template


app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "This is secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # จะเก็บ data ที่ไหน
models.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegisterForm() # สร้างฟอร์มสำหรับการลงทะเบียน
    if not form.validate_on_submit(): # ตรวจสอบฟอร์ม ส่งมาหรือไม่ ข้อมูลในฟอร์มถูกต้องไม่
        return render_template("register.html",form=form,)
    user = models.User() #เก็บข้อมูลผู้ใช้ใหม่
    form.populate_obj(user) # นำข้อมูลจากฟอร์มมาใส่ในอ็อบเจกต์ user
    user.password_hash = form.password.data  # ตั้งค่ารหัสผ่านให้อ่านยาก
    models.db.session.add(user) # เพิ่มผู้ใช้ใหม่ลงในฐานข้อมูล
    models.db.session.commit() # บันทึกการเปลี่ยนแปลงลงในฐานข้อมูล
    return flask.redirect(flask.url_for("index"))  # เสร็จแล้วไปหน้า index

@app.route("/login", methods=["GET", "POST"])
def login():
    form = forms.LoginForm() # สร้าง form
    if not form.validate_on_submit(): # ตรวจหน้า login
        return render_template("login.html",form=form,)
    user = models.User.query.filter_by(username=form.username.data).first() #หา user ในฐานข้อมูล
    if user and user.authenticate(form.password.data): # ตรวจรหัส
        login_user(user)
        return flask.redirect(flask.url_for("index"))
    return flask.redirect(flask.url_for("login", error="Invalid username or password")) # ถ้าข้อมูลไม่ถูกต้อง

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return flask.redirect(flask.url_for("login"))

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