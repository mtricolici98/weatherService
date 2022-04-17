from datetime import datetime
from tokenize import String

from sqlalchemy import Column, Integer, DateTime

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
    for_date = Column(DateTime, null=False)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"Weather in {self.city}, {self.country}: {self.condition}, {self.temperature}C (feels like)" \
               f" {self.feels_like}, wind speed {self.wind_speed} with humidity: {self.humidity}." \
               f" Data since {self.created_at.strftime('dd/MM/YY HH:mm')}."

    def __str__(self):
        return repr(self)
