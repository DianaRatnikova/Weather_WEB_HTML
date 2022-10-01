from flask import Flask
from webapp.weather import weather_by_city
from flask import render_template
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py') # откуда брать параметры конфигурации
    @app.route("/")

    def index():
        page_title = "Прогноз погоды"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"]) # вместо ("Moscow,Russia")
        if weather:
            weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
        else:
            weather_text ="Сервис временно недоступен "
        news_list = get_python_news()
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)
    return app

if __name__ == "__main__":
    app.run()