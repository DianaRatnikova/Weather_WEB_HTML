from urllib import request
import requests
#import api_key
from flask import current_app # для config

 
# Rename `os.environ` to `env` for nicer code
from os import environ as env
from dotenv import load_dotenv, find_dotenv #для .env

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
       # до файла конфигурации было "key": env['API_KEY'],
        "key": current_app.config['WEATHER_API_KEY'],
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
                    return None
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
    return False


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    print(f"API_KEY:  {env['API_KEY']}")
    weather = weather_by_city("Moscow,Russia")
    print(weather)
