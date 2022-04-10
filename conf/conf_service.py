import json
import os

conf_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf.json')


def get_config_from_file():
    with open(conf_file_path, 'r') as conf_file:
        data = json.loads(conf_file.read())
        return data
