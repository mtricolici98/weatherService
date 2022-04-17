import json

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

from conf import VIBER_AUTH_TOKEN
from logger import logger

bot_configuration = BotConfiguration(
    name='PythonSampleBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token=VIBER_AUTH_TOKEN
)
viber = Api(bot_configuration)


def set_webhook():
    import requests
    url = 'https://chatapi.viber.com/pa/set_webhook'
    api_key = VIBER_AUTH_TOKEN
    resp = requests.post(url,
                         data=json.dumps({
                             'url': f'https://cryptic-hollows-76455.herokuapp.com/viber',
                             "event_types": [
                                 "delivered",
                                 "seen",
                                 "failed",
                                 "subscribed",
                                 "unsubscribed",
                                 "conversation_started"
                             ],
                             "send_name": True,
                             "send_photo": True
                         }),
                         headers={'X-Viber-Auth-Token': api_key}
                         )
    logger.info(f"Viber answered with {resp.status_code} {resp.json()}")
