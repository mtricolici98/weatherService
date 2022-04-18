import json
from datetime import datetime
from typing import Collection

from flask import request, Response, Blueprint, render_template

from data.database import Session
from data.weather.models.WeatherRecord import WeatherRecord, WeatherForecast
from templates.icon_map import CONDITION_TO_ICON_MAP_DAY, CONDITION_TO_ICON_MAP_NIGH
from weather.service.location_service import get_coord_from_city, find_location_by_ip
from weather.service.weather_service import get_weather_current_data, get_weather_forecast_data

weather_data_blueprint = Blueprint('weather_data_blueprint', __name__)


def render_current(current_weather: WeatherRecord):
    icon_set = CONDITION_TO_ICON_MAP_DAY if 8 < datetime.now().hour < 18 else CONDITION_TO_ICON_MAP_NIGH
    icon = icon_set[current_weather.condition.split(',')[0]]
    return render_template('weather_widget.html',
                           for_date=current_weather.for_date.strftime(
                               '%d %b, %Y'
                           ),
                           city=current_weather.city,
                           temp=int(float(current_weather.temperature)),
                           image_icon=icon,
                           )


def render_forecast(forecast_data: Collection[WeatherForecast]):
    icon_set = CONDITION_TO_ICON_MAP_DAY
    template_forecast_data = []
    for forecast in forecast_data:
        icon = icon_set[forecast.condition.split(',')[0]]
        template_forecast_data.append(dict(
            for_date=forecast.for_date.strftime(
                '%d %b, %Y'
            ),
            city=forecast.city,
            temp_max=int(float(forecast.temperature_max)),
            temp_min=int(float(forecast.temperature_min)),
            image_icon=icon,
        ))
    return render_template('forecast_widget.html', forecast_data=template_forecast_data)


@weather_data_blueprint.route('/weather/current')
def get_current_weather():
    if request.args.get('city'):
        coord = get_coord_from_city(request.args.get('city'))
    else:
        coord = find_location_by_ip(request.remote_addr)
    session = Session()
    weather_data = get_weather_current_data(*coord, session=session)
    format = request.args.get('format', 'json')
    if format == 'json':
        return Response(json.dumps(weather_data.to_dict()), status=200)
    elif format == 'web':
        return Response(render_current(weather_data), status=200)


@weather_data_blueprint.route('/weather/forecast')
def get_forecast_weather():
    if request.args.get('city'):
        coord = get_coord_from_city(request.args.get('city'))
    else:
        coord = find_location_by_ip(request.remote_addr)
    session = Session()
    forecast_data = get_weather_forecast_data(*coord, session=session)
    format = request.args.get('format', 'json')
    if format == 'json':
        return Response(json.dumps([a.to_dict() for a in forecast_data]), status=200)
    elif format == 'web':
        return Response(render_forecast(forecast_data), status=200)
