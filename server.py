<<<<<<< HEAD
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
=======
from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route("/")
def index():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        return (f"Сейчас {weather['temp_C']}, "
                f"ощущается как {weather['FeelsLikeC']}")
    else:
        return ("Сервис временно недоступен ")


if __name__ == "__main__":
    app.run()
>>>>>>> ab9e2f5e97e5fde89851b9815fb16f3b4ca331fd
