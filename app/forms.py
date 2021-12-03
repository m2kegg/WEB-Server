from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.simple import BooleanField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    email = EmailField("E-mail:", validators=[Email()])
    passw = PasswordField("Пароль: ")
    submit = SubmitField()

class LoginForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    password = PasswordField("Пароль: ")
    rem = BooleanField("Запомнить меня")
    submit = SubmitField()   