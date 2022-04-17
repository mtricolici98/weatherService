from flask import Flask

from viber import set_webhook
from web_service.bot_service import viber_bot_blueprint
from web_service.weather_service import weather_data_blueprint

app = Flask(__name__)

app.register_blueprint(weather_data_blueprint)
app.register_blueprint(viber_bot_blueprint)


@app.before_first_request
def init_webhook():
    set_webhook()
