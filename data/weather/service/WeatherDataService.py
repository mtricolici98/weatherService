from datetime import datetime

from data.database import Session
from data.weather.models.WeatherRecord import WeatherRecord, WeatherForecast


class WeatherDataService:

    def __init__(self, session=None):
        self.session = session or Session()

    def from_one_call_json(self, city, data):
        current = self.register_weather(city, data['current'])
        for a in data['daily']:
            self.register_forecast(city, a)
        return current

    def register_weather(self, city, data):
        for_date = datetime.fromtimestamp(data['dt'])
        temp = data['temp']
        feels_like = data['feels_like']
        condition = f"{data['weather'][0]['main']}, {data['weather'][0]['description']}"
        humidity = data['humidity']
        wind_speed = data['wind_speed']
        weather = WeatherRecord(
            city=city,
            temperature=temp,
            feels_like=feels_like,
            condition=condition,
            humidity=humidity,
            wind_speed=wind_speed,
            for_date=for_date,
            created_at=datetime.now()
        )
        self.session.add(weather)
        self.session.refresh(weather)
        self.session.commit()
        return weather

    def register_forecast(self, city, data):
        for_date = datetime.fromtimestamp(data['dt'])
        for when in data['temp'].keys():
            temp = data['temp'][when]
            feels_like = data['feels_like'][when]
            condition = f"{data['weather'][0]['main']}, {data['weather'][0]['description']}"
            humidity = data['humidity']
            wind_speed = data['wind_speed']
            weather = WeatherForecast(
                city=city,
                when=when,
                temperature=temp,
                feels_like=feels_like,
                condition=condition,
                humidity=humidity,
                wind_speed=wind_speed,
                for_date=for_date,
                created_at=datetime.now()
            )
            self.session.add(weather)
            self.session.refresh(weather)
        self.session.commit()
