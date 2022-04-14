from data.database import Session


class WeatherService:

    def __init__(self, session=None):
        self.session = session or Session()
