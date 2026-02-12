import pytest
from music.client.config import Config, ServiceConfig, DatabaseConfig, AppConfig
from music.client.constants import (
    PROPERTY_NAME_NETWORK,
    PROPERTY_NAME_HOST,
    PROPERTY_NAME_PORT,
    PROPERTY_NAME_DRIVER_NAME,
    PROPERTY_NAME_USER,
    PROPERTY_NAME_PASSWORD,
    PROPERTY_NAME_DB_NAME,
    PROPERTY_NAME_SSL_MODE,
    PROPERTY_NAME_SERVICE,
    PROPERTY_NAME_DATABASE
)


class TestConfig:
    """Test suite for the Config base class"""

    @pytest.fixture
    def sample_config(self):
        """Fixture providing sample configuration dictionary"""
        return {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 123
        }

    def test_config_initialization(self, sample_config):
        """Test that Config initializes correctly"""
        config = Config(sample_config)
        assert config._config == sample_config

    def test_get_property_existing_key(self, sample_config):
        """Test getting an existing property"""
        config = Config(sample_config)
        assert config.get_property('key1') == 'value1'
        assert config.get_property('key2') == 'value2'
        assert config.get_property('key3') == 123

    def test_get_property_missing_key(self, sample_config):
        """Test getting a non-existent property returns None"""
        config = Config(sample_config)
        assert config.get_property('nonexistent') is None

    def test_get_property_none_value(self):
        """Test getting a property with None value"""
        config = Config({'key': None})
        assert config.get_property('key') is None


class TestServiceConfig:
    """Test suite for the ServiceConfig class"""

    @pytest.fixture
    def service_config_data(self):
        """Fixture providing sample service configuration"""
        return {
            PROPERTY_NAME_NETWORK: 'tcp',
            PROPERTY_NAME_HOST: 'localhost',
            PROPERTY_NAME_PORT: 50051
        }

    def test_service_config_inherits_from_config(self):
        """Test that ServiceConfig inherits from Config"""
        assert issubclass(ServiceConfig, Config)

    def test_service_config_network_property(self, service_config_data):
        """Test network property getter"""
        config = ServiceConfig(service_config_data)
        assert config.network == 'tcp'

    def test_service_config_host_property(self, service_config_data):
        """Test host property getter"""
        config = ServiceConfig(service_config_data)
        assert config.host == 'localhost'

    def test_service_config_port_property(self, service_config_data):
        """Test port property getter"""
        config = ServiceConfig(service_config_data)
        assert config.port == 50051

    def test_service_config_missing_properties(self):
        """Test that missing properties return None"""
        config = ServiceConfig({})
        assert config.network is None
        assert config.host is None
        assert config.port is None

    @pytest.mark.parametrize("network,host,port", [
        ('http', 'example.com', 8080),
        ('https', '127.0.0.1', 443),
        ('tcp', 'remote.server', 9000),
    ])
    def test_service_config_various_values(self, network, host, port):
        """Test ServiceConfig with various values"""
        config_data = {
            PROPERTY_NAME_NETWORK: network,
            PROPERTY_NAME_HOST: host,
            PROPERTY_NAME_PORT: port
        }
        config = ServiceConfig(config_data)
        assert config.network == network
        assert config.host == host
        assert config.port == port


class TestDatabaseConfig:
    """Test suite for the DatabaseConfig class"""

    @pytest.fixture
    def database_config_data(self):
        """Fixture providing sample database configuration"""
        return {
            PROPERTY_NAME_DRIVER_NAME: 'postgres',
            PROPERTY_NAME_USER: 'testuser',
            PROPERTY_NAME_DB_NAME: 'testdb',
            PROPERTY_NAME_SSL_MODE: 'disable',
            PROPERTY_NAME_PASSWORD: 'testpass',
            PROPERTY_NAME_HOST: 'localhost'
        }

    def test_database_config_inherits_from_config(self):
        """Test that DatabaseConfig inherits from Config"""
        assert issubclass(DatabaseConfig, Config)

    def test_database_config_driver_name_property(self, database_config_data):
        """Test driver_name property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.driver_name == 'postgres'

    def test_database_config_user_property(self, database_config_data):
        """Test user property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.user == 'testuser'

    def test_database_config_db_name_property(self, database_config_data):
        """Test db_name property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.db_name == 'testdb'

    def test_database_config_ssl_mode_property(self, database_config_data):
        """Test ssl_mode property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.ssl_mode == 'disable'

    def test_database_config_password_property(self, database_config_data):
        """Test password property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.password == 'testpass'

    def test_database_config_host_property(self, database_config_data):
        """Test host property getter"""
        config = DatabaseConfig(database_config_data)
        assert config.host == 'localhost'

    def test_database_config_missing_properties(self):
        """Test that missing properties return None"""
        config = DatabaseConfig({})
        assert config.driver_name is None
        assert config.user is None
        assert config.db_name is None
        assert config.ssl_mode is None
        assert config.password is None
        assert config.host is None

    @pytest.mark.parametrize("driver,user,dbname,host", [
        ('postgres', 'admin', 'production', 'db.example.com'),
        ('mysql', 'root', 'testdb', '127.0.0.1'),
        ('sqlite', 'user', 'local', 'localhost'),
    ])
    def test_database_config_various_values(self, driver, user, dbname, host):
        """Test DatabaseConfig with various values"""
        config_data = {
            PROPERTY_NAME_DRIVER_NAME: driver,
            PROPERTY_NAME_USER: user,
            PROPERTY_NAME_DB_NAME: dbname,
            PROPERTY_NAME_HOST: host,
            PROPERTY_NAME_PASSWORD: 'pass',
            PROPERTY_NAME_SSL_MODE: 'require'
        }
        config = DatabaseConfig(config_data)
        assert config.driver_name == driver
        assert config.user == user
        assert config.db_name == dbname
        assert config.host == host


class TestAppConfig:
    """Test suite for the AppConfig class"""

    @pytest.fixture
    def full_config_data(self):
        """Fixture providing complete application configuration"""
        return {
            PROPERTY_NAME_SERVICE: {
                PROPERTY_NAME_NETWORK: 'tcp',
                PROPERTY_NAME_HOST: 'localhost',
                PROPERTY_NAME_PORT: 50051
            },
            PROPERTY_NAME_DATABASE: {
                PROPERTY_NAME_DRIVER_NAME: 'postgres',
                PROPERTY_NAME_USER: 'testuser',
                PROPERTY_NAME_DB_NAME: 'testdb',
                PROPERTY_NAME_SSL_MODE: 'disable',
                PROPERTY_NAME_PASSWORD: 'testpass',
                PROPERTY_NAME_HOST: 'localhost'
            }
        }

    def test_app_config_initialization(self, full_config_data):
        """Test that AppConfig initializes correctly"""
        config = AppConfig(full_config_data)
        assert config._service_config is not None
        assert config._database_config is not None

    def test_app_config_service_config_property(self, full_config_data):
        """Test service_config property getter"""
        config = AppConfig(full_config_data)
        assert isinstance(config.service_config, ServiceConfig)
        assert config.service_config.host == 'localhost'
        assert config.service_config.port == 50051

    def test_app_config_database_config_property(self, full_config_data):
        """Test database_config property getter"""
        config = AppConfig(full_config_data)
        assert isinstance(config.database_config, DatabaseConfig)
        assert config.database_config.host == 'localhost'
        assert config.database_config.user == 'testuser'

    def test_app_config_creates_service_config_instance(self, full_config_data):
        """Test that AppConfig creates ServiceConfig instance"""
        config = AppConfig(full_config_data)
        service_config = config.service_config
        assert service_config.network == 'tcp'
        assert service_config.host == 'localhost'
        assert service_config.port == 50051

    def test_app_config_creates_database_config_instance(self, full_config_data):
        """Test that AppConfig creates DatabaseConfig instance"""
        config = AppConfig(full_config_data)
        database_config = config.database_config
        assert database_config.driver_name == 'postgres'
        assert database_config.user == 'testuser'
        assert database_config.db_name == 'testdb'
        assert database_config.ssl_mode == 'disable'
        assert database_config.password == 'testpass'
        assert database_config.host == 'localhost'

    def test_app_config_with_empty_sections(self):
        """Test AppConfig with empty configuration sections"""
        config_data = {
            PROPERTY_NAME_SERVICE: {},
            PROPERTY_NAME_DATABASE: {}
        }
        config = AppConfig(config_data)
        assert config.service_config is not None
        assert config.database_config is not None
        assert config.service_config.host is None
        assert config.database_config.user is None
