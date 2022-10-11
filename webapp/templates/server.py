from flask import Flask
from webapp.templates.weather import weather_by_city
from flask import render_template
from webapp.templates.python_org_news import get_python_news


app = Flask(__name__)


@app.route("/")
def index():
    page_title = "Прогноз погоды"
    weather = weather_by_city("Moscow,Russia")
    if weather:
        weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text ="Сервис временно недоступен "
    news_list = get_python_news()
    return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)

if __name__ == "__main__":
    app.run()