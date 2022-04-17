from datetime import datetime, timedelta

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
        self.session.commit()
        return weather

    def register_forecast(self, city, data):
        for_date = datetime.fromtimestamp(data['dt'])
        for when in data['feels_like'].keys():
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
        self.session.commit()

    def get_within_15_minutes_from_db(self, city):
        try:
            return self.session.query(WeatherRecord).filter(
                WeatherRecord.created_at >= datetime.now() - timedelta(minutes=15)).filter(
                WeatherRecord.city == city).one()
        except Exception as ex:
            return None

    def get_forecast_from_1_hour(self, city):
        try:
            from sqlalchemy.sql.functions import max
            return self.session.query(WeatherForecast).filter(
                WeatherForecast.created_at >= datetime.now() - timedelta(hours=1)).filter(
                WeatherForecast.city == city).filter(WeatherForecast.for_date > datetime.now()).having(
                WeatherForecast.created_at == max(WeatherForecast.created_at)) \
                .order_by(WeatherForecast.for_date)
        except Exception as ex:
            return None
