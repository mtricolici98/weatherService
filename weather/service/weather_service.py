import requests

from conf import WEATHER_API_KEY


def get_locaiton():
    url = 'https://ipapi.co/json'
    data = requests.get(url)
    info = data.json()
    location_info = ", ".join([info.get('city'), info.get('country')])
    return location_info, info.get('latitude'), info.get('longitude')


def get_weather(lat, lon):
    weather_url = 'https://api.openweathermap.org/data/2.5/onecall'
    resp = requests.get(weather_url, params={
        'lat': lat,
        'lon': lon,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    })
    return resp.json()


if __name__ == '__main__':
    location, lat, lon = get_locaiton()
    data = get_weather(lat, lon)
    temp = data.get('current', {}).get('temp')
    temp_like = data.get('current', {}).get('feels_like')
    weather = data.get('current', {}).get('weather')[0].get('main')
    print(f'Currently in {location}: {weather}, temperature {temp}C, feels like {temp_like}C')
