from flask import request, Response

from app import app
from weather.service.location_service import get_coord_from_city


@app.route('/weather/current')
def get_current_weather():
    request
    if request.args.get('city'):
        coord = get_coord_from_city()

    return Response()


@app.route('/weather/forecast')
def get_forecast_weather():
    request
    return Response()
