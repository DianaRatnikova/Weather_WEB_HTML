from flask import Flask
from webapp.weather import weather_by_city
from flask import render_template
from webapp.python_org_news import get_python_news
from webapp.model import db, News

# добавляем страницк логина
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py') # откуда брать параметры конфигурации
    db.init_app(app)
   
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
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app


if __name__ == "__main__":
    app.run()