from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String, Date

from data.database import Base


class WeatherRecord(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    country = Column(String)
    temperature = Column(String)
    feels_like = Column(String)
    condition = Column(String)
    humidity = Column(String)
    wind_speed = Column(String)
    for_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"Weather in {self.city}:\n {self.condition}, {int(float(self.temperature))}C (feels like" \
               f" {int(self.feels_like)}C). \n Wind speed {self.wind_speed}m/s with humidity: {self.humidity}%. \n" \
               f" Data since {self.created_at.strftime('%m/%d, %H:%M')}."

    def __str__(self):
        return repr(self)

    def to_dict(self):
        return dict(
            city=self.city,
            country=self.country,
            temperature=self.temperature,
            feels_like=self.feels_like,
            condition=self.condition,
            humidity=self.humidity,
            wind_speed=self.wind_speed,
            for_date=self.for_date.strftime('%m/%d/%Y'),
            created_at=self.created_at.strftime('%m/%d/%Y, %H:%M'),
        )


class WeatherForecast(Base):
    __tablename__ = 'weather_forecast'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    temperature_min = Column(String)
    temperature_max = Column(String)
    condition = Column(String)
    humidity = Column(String)
    wind_speed = Column(String)
    for_date = Column(Date)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"Weather for {self.for_date.strftime('%m/%d')} in {self.city} :\n {self.condition} \n " \
               f"Min temp: {int(float(self.temperature_min))}C \n" \
               f"Max temp: {int(float(self.temperature_max))}C \n" \
               f"{self.wind_speed}m/s with humidity: {self.humidity}%. \n" \
               f" Data since {self.created_at.strftime('%m/%d, %H:%M')}."

    def __str__(self):
        return repr(self)

    def to_dict(self):
        return dict(
            city=self.city,
            temperature_min=self.temperature_min,
            temperature_max=self.temperature_max,
            condition=self.condition,
            humidity=self.humidity,
            wind_speed=self.wind_speed,
            for_date=self.for_date.strftime('%m/%d/%Y'),
            created_at=self.created_at.strftime('%m/%d/%Y, %H:%M'),
        )
