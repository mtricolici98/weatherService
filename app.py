from flask import Flask

from web_service.weather_service import weather_data_blueprint

app = Flask(__name__)

app.register_blueprint(weather_data_blueprint)
