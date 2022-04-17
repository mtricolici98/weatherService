from data.database import Session
from data.weather.models.WeatherRecord import WeatherRecord


class WeatherDataService:

    def __init__(self, session=None):
        self.session = session or Session()

    def from_one_call_json(self, data):
        WeatherRecord(
            city=data.get(),
            country=data.get(),
            temperature=data.get(),
            feels_like=data.get(),
            condition=data.get(),
            humidity=data.get(),
            wind_speed=data.get(),
            for_date=data.get(),
        )

    def register_weather(self, data):
        pass
