from flask import request, Response

from app import app


@app.route('/weather/current')
def get_current_weather():
    request
    return Response()


@app.route('/weather/forecast')
def get_forecast_weather():
    request
    return Response()
