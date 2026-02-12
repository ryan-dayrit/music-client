import pytest
from music.client.constants import (
    CONFIG_FILE_PATH,
    PROPERTY_NAME_NETWORK,
    PROPERTY_NAME_HOST,
    PROPERTY_NAME_PORT,
    PROPERTY_NAME_DRIVER_NAME,
    PROPERTY_NAME_USER,
    PROPERTY_NAME_PASSWORD,
    PROPERTY_NAME_DB_NAME,
    PROPERTY_NAME_SSL_MODE,
    PROPERTY_NAME_SERVICE,
    PROPERTY_NAME_DATABASE,
    SOURCE_SERVICE,
    SOURCE_DATABASE,
    DEFAULT_POSTGRESQL_PORT,
    QUERY_GET_ALBUMS
)


class TestConstants:
    """Test suite for constants module"""

    def test_config_file_path_constant(self):
        """Test CONFIG_FILE_PATH constant"""
        assert CONFIG_FILE_PATH == "config.yaml"
        assert isinstance(CONFIG_FILE_PATH, str)

    def test_property_name_constants(self):
        """Test all PROPERTY_NAME constants are strings"""
        assert PROPERTY_NAME_NETWORK == "network"
        assert PROPERTY_NAME_HOST == "host"
        assert PROPERTY_NAME_PORT == "port"
        assert PROPERTY_NAME_DRIVER_NAME == "driver_name"
        assert PROPERTY_NAME_USER == "user"
        assert PROPERTY_NAME_PASSWORD == "password"
        assert PROPERTY_NAME_DB_NAME == "db_name"
        assert PROPERTY_NAME_SSL_MODE == "ssl_mode"
        assert PROPERTY_NAME_SERVICE == "service"
        assert PROPERTY_NAME_DATABASE == "database"

    def test_source_constants(self):
        """Test SOURCE constants"""
        assert SOURCE_SERVICE == "service"
        assert SOURCE_DATABASE == "database"
        assert isinstance(SOURCE_SERVICE, str)
        assert isinstance(SOURCE_DATABASE, str)

    def test_default_postgresql_port(self):
        """Test DEFAULT_POSTGRESQL_PORT constant"""
        assert DEFAULT_POSTGRESQL_PORT == "5432"
        assert isinstance(DEFAULT_POSTGRESQL_PORT, str)

    def test_query_get_albums(self):
        """Test QUERY_GET_ALBUMS constant"""
        assert QUERY_GET_ALBUMS == "SELECT id, title, artist, price FROM music.albums;"
        assert isinstance(QUERY_GET_ALBUMS, str)
        assert "SELECT" in QUERY_GET_ALBUMS
        assert "music.albums" in QUERY_GET_ALBUMS

    def test_all_constants_are_immutable_types(self):
        """Test that all constants are immutable types (strings)"""
        constants = [
            CONFIG_FILE_PATH,
            PROPERTY_NAME_NETWORK,
            PROPERTY_NAME_HOST,
            PROPERTY_NAME_PORT,
            PROPERTY_NAME_DRIVER_NAME,
            PROPERTY_NAME_USER,
            PROPERTY_NAME_PASSWORD,
            PROPERTY_NAME_DB_NAME,
            PROPERTY_NAME_SSL_MODE,
            PROPERTY_NAME_SERVICE,
            PROPERTY_NAME_DATABASE,
            SOURCE_SERVICE,
            SOURCE_DATABASE,
            DEFAULT_POSTGRESQL_PORT,
            QUERY_GET_ALBUMS
        ]
        for constant in constants:
            assert isinstance(constant, str)
