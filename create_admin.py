from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

'''
Создаём апликейшн, в его контексте 
запрашиваем имя пользователя, проверяем, 
что такого пользователя нет в БД.
Дважды запрашиваем пароль, сравниваем два ввода.

Создаём объект пользователя, записываемя в него имя и пароль
'''

app = create_app()

with app.app_context():
    username = input('Введите имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        print('Пароли неодинаковые! ')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    # print('User with id {} added'.format(new_user.id))
    print('Создан пользователь с id = {}'.format(new_user.id))