from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Заповніть логін"),
            Length(min=3, message="Треба щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Заповніть пароль)"),
        ],
    )
    submit = SubmitField("submit")


class RegisterForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Заповніть логін"),
            Length(min=3, message="Треба щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Заповніть пароль)"),
        ],
    )
    password_confirm = PasswordField(
        "Підтвердіть пароль",
        validators=[
            DataRequired("Заповніть пароль)"),
            EqualTo('password')
        ],
    )
    submit = SubmitField("submit")
