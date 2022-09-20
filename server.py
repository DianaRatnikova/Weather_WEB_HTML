from flask import Flask
from weather import weather_by_city
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    page_title = "Прогноз погоды"
    weather = weather_by_city("Moscow,Russia")
    if weather:
        weather_text = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text ="Сервис временно недоступен "

    return render_template('index.html', page_title=page_title, weather_text=weather_text)

if __name__ == "__main__":
    app.run()