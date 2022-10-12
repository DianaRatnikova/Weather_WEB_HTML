from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# для работы с паролем:
# generate_password_hash - шифрование пароля только в одну сторону
from werkzeug.security import generate_password_hash, check_password_hash
'''
Модель описывает объект, который мы хотим сохранять в БД 
и получать из БД. SQLAlchemy будет делать 
всю работу по переводу с привычного нам python-синтаксиса 
на язык SQL.
'''

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

# что выведет Питон при print(News)
    def __repr__(self): # "магический метод Питона"
        return '<News {} {}>'.format(self.title, self.url)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

# зашифровка пароля
    def set_password(self, password):
        self.password = generate_password_hash(password)

# сравнение паролей, результат - True или False
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User name = {}, id = {}>'.format(self.username, self.id)

    @property
    def is_admin(self):
        return self.role == 'admin'   