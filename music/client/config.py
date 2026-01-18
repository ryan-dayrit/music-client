from music.client.constants import (
    PROPERTY_NAME_NETWORK,
    PROPERTY_NAME_HOST,
    PROPERTY_NAME_PORT,
    PROPERTY_NAME_DRIVER_NAME,
    PROPERTY_NAME_DB_NAME,
    PROPERTY_NAME_PASSWORD,
    PROPERTY_NAME_USER,
    PROPERTY_NAME_SSL_MODE,
    PROPERTY_NAME_SERVICE,
    PROPERTY_NAME_DATABASE
)

class Config(object):
    def __init__(self, conf):
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): 
            return None 
        return self._config[property_name]
    
class ServiceConfig(Config):
    @property
    def network(self):
        return self.get_property(PROPERTY_NAME_NETWORK)

    @property
    def host(self):
        return self.get_property(PROPERTY_NAME_HOST)
    
    @property
    def port(self):
        return self.get_property(PROPERTY_NAME_PORT)
    
class DatabaseConfig(Config): 
    @property
    def driver_name(self):
        return self.get_property(PROPERTY_NAME_DRIVER_NAME)

    @property
    def user(self):
        return self.get_property(PROPERTY_NAME_USER)

    @property
    def db_name(self):
        return self.get_property(PROPERTY_NAME_DB_NAME)
    
    @property
    def ssl_mode(self):
        return self.get_property(PROPERTY_NAME_SSL_MODE)
    
    @property
    def password(self):
        return self.get_property(PROPERTY_NAME_PASSWORD)
    
    @property
    def host(self):
        return self.get_property(PROPERTY_NAME_HOST)

class AppConfig():
    def __init__(self, conf):
        self._service_config = ServiceConfig(conf[PROPERTY_NAME_SERVICE])
        self._database_config = DatabaseConfig(conf[PROPERTY_NAME_DATABASE])

    @property
    def service_config(self):
        return self._service_config

    @property
    def database_config(self):
        return self._database_config