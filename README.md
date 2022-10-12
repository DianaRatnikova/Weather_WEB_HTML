# Weather_WEB_HTML
Выполнены 4трека по веб-разработке LearnPython

Приложение показывает актуальную температуру в Москве: фактическую и "по ощущениям".
Показывает актуальные новости по Питону


## Сборка репозитория и локальный запуск
Выполните в консоли:
```
https://github.com/DianaRatnikova/Weather_WEB_HTML
pip install -r requirments.txt
```
 
### Настройка
Создайте файл webapp/templates/config.py и добавьте туда следующие настройки:
```
WEATHER_DEFAULT_CITY = "Ваш город и страна, например Moscow,Russia"
WEATHER_API_KEY = "Ваш API Ключ с ресурса worldweatheronline.com"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "Ваш секретный ключ"

```
### Создание базы данных
Из корня проекта запустите конструктор базы данных:
```
python create_db.py
```
### Создание новой учётной записи для доступа к серверу
Из корня проекта запустите конструктор базы данных:
```
py create_admin.py
```
После этого введите имя пользователя и пароль дважды.
После сообщения "Создан пользователь с id = ...." в базу данных будет добавлена новая учтная запись.
Пример вывода:
Введите имя пользователя: Diana
Введите пароль:
Повторите пароль:
Создан пользователь с id = 1


### Запуск
Чтобы запустить скрипт, выполните команду с корне проекта:
```
set FLASK_APP=webapp&&set FLAK_ENV=development&&set FLASK_DEBUG=1&&flask run
```


Открыть в браузере появившийся адрес, например * Running on http://127.0.0.1:5000 

Результат - вывод сообщения о температуре, либо о невозможности подключиться к серверу
Доступны страницы:
http://127.0.0.1:5000
http://127.0.0.1:5000/login
http://127.0.0.1:5000/admin
http://127.0.0.1:5000/logout


