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


def get_weather_current_data(city, lat, lon):
    wds = WeatherDataService()
    existing = wds.get_within_15_minutes_from_db(city)
    if existing:
        return str(existing)
    weather = get_weather(lat, lon)
    result = WeatherDataService().from_one_call_json(city, weather)
    return str(result)


def get_weather_forecast_data(city, lat, lon):
    wds = WeatherDataService()
    existing = wds.get_forecast_from_1_hour(city)
    if existing:
        return "\n\n".join(str(e) for e in existing)
    weather = get_weather(lat, lon)
    WeatherDataService().from_one_call_json(city, weather)
    return "\n\n".join(str(e) for e in wds.get_forecast_from_1_hour(city))
