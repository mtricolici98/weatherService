import os

WEATHER_API_KEY = ''
DATABASE_KEY = ''

if not WEATHER_API_KEY:
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', None)
    if not WEATHER_API_KEY:
        from conf_service import get_config_from_file

        conf = get_config_from_file()
        WEATHER_API_KEY = conf['WEATHER_API_KEY']
