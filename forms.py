from wtforms_sqlalchemy.orm import model_form
from flask_wtf import FlaskForm
from wtforms import Field, widgets,validators, fields
import models
from flask_wtf import FlaskForm, file

BaseUserForm = model_form(models.User, # ฟังก์ชันนี้จะสร้างฟอร์มโดยอัตโนมัติจากโมเดล SQLAlchemy
            base_class=FlaskForm,
            exclude=["created_date", "updated_date", "status", "_password_hash"],
            db_session=models.db.session,) # ใช้ session ของฐานข้อมูลจากโมเดล

class RegisterForm(BaseUserForm):
    username = fields.StringField("username", [validators.DataRequired()]) #กำหนดลักษณะที่กรอกข้อมูล
    password = fields.PasswordField("password", [validators.DataRequired(), validators.length(min=6)]) #กำหนดลักษณะที่กรอกข้อมูล
    
class LoginForm(FlaskForm):
    username = fields.StringField("username", [validators.DataRequired()])
    password = fields.PasswordField("password", [validators.DataRequired()])