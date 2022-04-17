import requests

from conf import WEATHER_API_KEY
from data.weather.service.WeatherDataService import WeatherDataService


def get_weather(lat, lon):
    weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
    resp = requests.get(weather_url, params={
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'exclude': ['minutely', 'hourly', 'alerts']
    })
    return resp.json()


def get_weather_data(city, lat, lon):
    wds = WeatherDataService()
    existing = wds.get_within_15_minutes_from_db(city)
    if existing:
        return str(existing)
    weather = get_weather(lat, lon)
    result = WeatherDataService().from_one_call_json(city, weather)
    return str(result)
