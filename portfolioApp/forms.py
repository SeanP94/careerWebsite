from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class CreateUser(FlaskForm):
    username = StringField(label="User Name")
    password1 = PasswordField(label="Password")
    password2 = PasswordField(label="Confirm Password")
    submit = SubmitField(label='Create Account')

class LoginUser(FlaskForm):
    username = StringField(label="User Name")
    password = PasswordField(label="Password")
    submit = SubmitField(label='Create Account')