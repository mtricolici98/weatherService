from sqlalchemy import String, Integer, Column

from data import Base


class LocationSession(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    city = Column(String)
    lat = Column(String)
    lon = Column(String)
