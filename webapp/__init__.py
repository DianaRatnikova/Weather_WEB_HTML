from flask import Flask, flash, render_template,  redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from webapp.weather import weather_by_city
from flask import render_template
from webapp.python_org_news import get_python_news
from webapp.model import db, News, User

'''
from flask import Flask, render_template, flash, redirect, url_for
flash - позволяет передавать сообщения между route-ами
redirect - делает перенаправление пользователя на другую страницу
url_for - помогает получить url по имени функции, которая этот url обрабатывает
'''


# добавляем страницк логина
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py') # откуда брать параметры конфигурации
    db.init_app(app)
   
# Flask-login
    login_manager = LoginManager() # создаём экземпляр логин-менеджера
    login_manager.init_app(app)    # делаем инит
    # как будет наз-ся ф-я, кот. занимается логином пользователя
    login_manager.login_view = 'login'

# load_user - ф-я, кот будет получать нужного пользователя по ИД
# при каждом заходе на страницу осуществляется запрос к базе данных
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route("/")

    def index():
        page_title = "Прогноз погоды"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"]) # вместо ("Moscow,Russia")
        if weather:
            weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
        else:
            weather_text ="Сервис временно недоступен "
        # вместо get_python_news():
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)

    @app.route('/login')

    def login():
        print(current_user)
        # если юзер залогинен, то он не сможет зайти на страницу http://127.0.0.1:5000/login
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

# обработка формы логина
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

# у логаута не будет отдельной страницы, просто перенаправляет в индекс
    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required 
# декоратор проверяет, залогинен ли юзер. Только после этого работает функция
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'

    return app


if __name__ == "__main__":
    app.run()