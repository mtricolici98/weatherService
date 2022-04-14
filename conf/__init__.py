import os

from conf.conf_service import get_config_from_file

WEATHER_API_KEY = ''
DATABASE_URL = ''
VIBER_AUTH_TOKEN = ''

if not WEATHER_API_KEY:
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', None)
    if not WEATHER_API_KEY:
        conf = get_config_from_file()
        WEATHER_API_KEY = conf['WEATHER_API_KEY']

if not DATABASE_URL:
    uri = os.getenv("DATABASE_URL")  # postgres is the default database, you can create more databases
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        DATABASE_URL = uri
    else:
        conf = get_config_from_file()
        DATABASE_URL = conf['DATABASE_URL']

if not VIBER_AUTH_TOKEN:
    token = os.getenv("VIBER_AUTH_TOKEN")  # postgres is the default database, you can create more databases
    if not token:
        conf = get_config_from_file()
        VIBER_AUTH_TOKEN = conf['VIBER_AUTH_TOKEN']
