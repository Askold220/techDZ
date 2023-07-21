from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Логін треба заповнити"),
            Length(min=3, message="Тре щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Пароль давай)"),
        ],
    )
    submit = SubmitField("Тисни мене")

class RegisterForm(FlaskForm):
    login = StringField(
        "Логін",
        validators=[
            DataRequired("Логін треба заповнити"),
            Length(min=3, message="Тре щонайменше 3 символи."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired("Пароль давай)"),
        ],
    )
    password_confirm = PasswordField(
        "Підтвердіть пароль",
        validators=[
            DataRequired("Пароль давай)"),
            EqualTo('password')
        ],
    )
    submit = SubmitField("Тисни мене")

class PostForm(FlaskForm):
    
    header = StringField(
        "Заголовок",
        validators=[
            DataRequired("Текст треба заповнити"),
        ],
    )
    
    body = TextAreaField(
        "Текст",
        validators=[
            DataRequired("Текст треба заповнити"),
            Length(min=10, message="Треба щонайменше 10 символи."),
        ],
    )
    
    submit = SubmitField("Підтвердити")