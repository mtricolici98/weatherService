import requests

from conf import WEATHER_API_KEY


def get_weather(lat, lon):
    weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
    resp = requests.get(weather_url, params={
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    })
    return resp.json()
