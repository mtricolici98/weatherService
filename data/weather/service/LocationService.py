from data.database import Session
from data.weather.models.LocationSession import LocationSession


class LocationSessionService:

    def __init__(self, session=None):
        self.session: Session = session or Session()

    def register_user_session(self, user_id, city, lat, lon):
        self.delete_session_for_user(user_id)
        loc_session = LocationSession(
            user_id=user_id,
            city=city,
            lat=lat,
            lon=lon,
        )
        self.session.add(loc_session)
        self.session.commit()
        return loc_session

    def get_session_for_user(self, user_id):
        try:
            return self.session.query(LocationSession).filter(LocationSession.user_id == user_id).one()
        except Exception as ex:
            return None

    def delete_session_for_user(self, user_id):
        try:
            if self.session.query(LocationSession).filter(LocationSession.user_id == user_id).count() == 1:
                self.session.delete(
                    self.session.query(LocationSession).filter(LocationSession.user_id == user_id).one())
        except Exception as ex:
            return None
