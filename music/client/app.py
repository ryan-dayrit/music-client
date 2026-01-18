import yaml

from music.client.config import AppConfig 
from music.client.constants import CONFIG_FILE_PATH 

class App(object):
    def __init__(self):
        try:
            with open(CONFIG_FILE_PATH, 'r') as file:
                data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError:
            print(f"Error: The file {CONFIG_FILE_PATH} was not found.")

        self._config = AppConfig(data)

    def run(self, source):
        print(f"service_config.network: {self._config.service_config.network}")
        print(f"database_config.db_name: {self._config.database_config.db_name}")
        print(f"source: {source}")
