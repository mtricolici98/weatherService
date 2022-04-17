import json

from flask import request, Response, Blueprint

from weather.service.location_service import get_coord_from_city, find_location_by_ip
from weather.service.weather_service import get_weather_current_data, get_weather_forecast_data

weather_data_blueprint = Blueprint('weather_data_blueprint', __name__)


@weather_data_blueprint.route('/weather/current')
def get_current_weather():
    if request.args.get('city'):
        coord = get_coord_from_city(request.args.get('city'))
    else:
        coord = find_location_by_ip(request.remote_addr)
    response_data = get_weather_current_data(*coord)
    return Response(json.dumps(str(response_data)), status=200)


@weather_data_blueprint.route('/weather/forecast')
def get_forecast_weather():
    if request.args.get('city'):
        coord = get_coord_from_city(request.args.get('city'))
    else:
        coord = find_location_by_ip(request.remote_addr)
    response_data = get_weather_forecast_data(*coord)
    return Response(json.dumps(str(response_data)), status=200)
