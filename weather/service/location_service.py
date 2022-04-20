import requests
from viberbot.api.messages import LocationMessage, TextMessage

from conf import WEATHER_API_KEY
from logger import logger


class IpLocationNotFound(Exception):
    pass


def find_location_by_ip(ip_addr):
    logger.info(f"Using {ip_addr} for location")
    return get_location_by_ip_addr(ip_addr)


def get_location_by_ip_addr(ip_addr):
    url = f'http://ip-api.com/json/{ip_addr}'
    data = requests.get(url)
    info = data.json()
    if info.get('status') == 'fail':
        raise IpLocationNotFound(f'Could not find location for IP {ip_addr}')
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
    return info[0]['name'], info[0]['lat'], info[0]['lon']


def get_location_from_viber_location(viber_message: LocationMessage):
    return get_city_from_coord(viber_message.location.latitude,
                               viber_message.location.longitude), \
           viber_message.location.latitude, viber_message.location.longitude


def get_location_from_viber_message(cityInfo: TextMessage):
    return get_coord_from_city(cityInfo.text)
