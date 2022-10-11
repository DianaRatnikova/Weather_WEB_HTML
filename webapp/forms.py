from flask_wtf import FlaskForm
# импортируем типы полей: строковое, для ввода пароля и для сабмита
from wtforms import StringField, PasswordField, SubmitField
# валидатор - позволяет избегать ручных проверок
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-primary"})