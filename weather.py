<<<<<<< HEAD
from urllib import request
import requests
import api_key


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": api_key.API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params) # сходить на сервер 
        result.raise_for_status()
        weather = result.json()  # вернуть результат
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)
=======
from urllib import request
import requests
import api_key


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": api_key.API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params) # сходить на сервер 
        result.raise_for_status()
        weather = result.json()  # вернуть результат
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException):
        print("Сетевая ошибка")
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)
>>>>>>> ab9e2f5e97e5fde89851b9815fb16f3b4ca331fd