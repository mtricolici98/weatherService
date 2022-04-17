import requests
from viberbot.api.messages import LocationMessage, TextMessage

from conf import WEATHER_API_KEY


def find_location_by_ip(request):
    ip_addr = request.remote_addr
    return get_location_by_ip_addr(ip_addr)


def get_location_by_ip_addr(ip_addr):
    url = f'http://ip-api.com/json/{ip_addr}'
    data = requests.get(url)
    info = data.json()
    location_info = ", ".join([info.get('city'), info.get('country')])
    return location_info, info.get('lat'), info.get('lon')


def get_city_from_coord(lat, lon):
    url = f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={1}&appid={WEATHER_API_KEY}'
    data = requests.get(url)
    info = data.json()
    location_info = info[0]['name']
    return location_info


def get_coord_from_city(locationInfo):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={locationInfo}&appid={WEATHER_API_KEY}'
    data = requests.get(url)
    info = data.json()
    location_info = info[0]['name']
    return location_info[0]['name'], location_info[0]['lat'], location_info[0]['lon']


def get_location_from_viber_location(viber_message: LocationMessage):
    return get_city_from_coord(viber_message.location.lat,
                               viber_message.location.lon), \
           viber_message.location.lat, viber_message.location.lon


def get_location_from_viber_message(cityInfo: TextMessage):
    return get_coord_from_city(cityInfo.text)
