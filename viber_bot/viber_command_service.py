from viberbot.api.messages import TextMessage, KeyboardMessage, LocationMessage
from viberbot.api.user_profile import UserProfile
from viberbot.api.viber_requests import ViberMessageRequest

from data.weather.models.LocationSession import LocationSession
from data.weather.service.LocationService import LocationSessionService
from logger import logger
from weather.service.location_service import get_coord_from_city, get_location_from_viber_location


def register_location(message: ViberMessageRequest, sender: UserProfile):
    return TextMessage(text='Order placed')


def get_menu():
    weather_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "ActionType": "reply",
                "ActionBody": "change_location",
                "ReplyType": "message",
                "Text": "Current weather"
            },
            {
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "ActionType": "reply",
                "ActionBody": "current",
                "ReplyType": "message",
                "Text": "Current weather"
            },
            {
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "ActionType": "reply",
                "ActionBody": "current",
                "ReplyType": "message",
                "Text": "Forecast"
            },
        ]
    }

    return KeyboardMessage(tracking_data=f'weather_info', keyboard=weather_keyboard)


def get_welcome():
    return TextMessage(tracking_data=f'welcome', text='Welcome, type /start to see the instruction')


def get_init_loc(error=False):
    if not error:
        message_text = 'Send me your location, or type the name of the city, example: London, UK'
    else:
        message_text = 'Oops, something went wrong, please try again.'
    return TextMessage(tracking_data=f'register_location', text=message_text)


def receive_command(message_req: ViberMessageRequest):
    tracking_data = message_req.message.tracking_data
    if tracking_data and tracking_data == 'weather_info':
        user_message = message_req.message.text
        if user_message == 'current':
            return get_menu()
        elif user_message == 'forecast':
            return get_menu()
    elif tracking_data and tracking_data == 'register_location':
        if isinstance(message_req.message, TextMessage):
            try:
                info = get_coord_from_city(message_req.message.text)
                lss = LocationSessionService()
                lss.register_user_session(message_req.sender.id, *info)
                return get_menu()
            except Exception as ex:
                logger.exceptiion(ex)
                return get_init_loc(error=True)
        elif isinstance(message_req.message, LocationMessage):
            try:
                info = get_location_from_viber_location(message_req.message)
                lss = LocationSessionService()
                lss.register_user_session(message_req.sender.id, *info)
                return get_menu()
            except Exception as ex:
                logger.exceptiion(ex)
                return get_init_loc(error=True)
    elif tracking_data and tracking_data == 'welcome':
        if message_req.message.text.lower().strip() == '/start':
            return get_init_loc()
    else:
        return get_welcome()
