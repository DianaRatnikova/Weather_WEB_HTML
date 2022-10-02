from flask_sqlalchemy import SQLAlchemy
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