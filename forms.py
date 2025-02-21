from wtforms_sqlalchemy.orm import model_form
from flask_wtf import FlaskForm
from wtforms import Field,validators, fields
import models
from flask_wtf import FlaskForm

BaseUserForm = model_form(models.User,
                base_class=FlaskForm,
                exclude=["created_date", "updated_date", "status", "_password_hash"],
                db_session=models.db.session,)

class RegisterForm(BaseUserForm):
    username = fields.StringField("username", [validators.DataRequired(), validators.length(min=6)])
    password = fields.PasswordField("password", [validators.DataRequired(), validators.length(min=6)])
    name = fields.StringField("name", [validators.DataRequired(), validators.length(min=6)])