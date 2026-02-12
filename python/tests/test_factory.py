import pytest
from unittest.mock import Mock, MagicMock
from music.repository.factory import get_repository
from music.repository.postgres import PostgresRepository
from music.repository.grpc import GRPCRepository
from music.client.constants import SOURCE_SERVICE, SOURCE_DATABASE


class TestRepositoryFactory:
    """Test suite for the repository factory function"""

    @pytest.fixture
    def mock_service_config(self):
        """Fixture providing mock service configuration"""
        config = Mock()
        config.host = 'localhost'
        config.port = 50051
        return config

    @pytest.fixture
    def mock_database_config(self):
        """Fixture providing mock database configuration"""
        config = Mock()
        config.db_name = 'testdb'
        config.user = 'testuser'
        config.password = 'testpass'
        config.host = 'localhost'
        return config

    @pytest.fixture
    def mock_app_config(self, mock_service_config, mock_database_config):
        """Fixture providing mock application configuration"""
        config = Mock()
        config.service_config = mock_service_config
        config.database_config = mock_database_config
        return config

    def test_get_repository_with_service_source(self, mock_app_config):
        """Test that get_repository returns GRPCRepository for 'service' source"""
        repository = get_repository(mock_app_config, SOURCE_SERVICE)
        assert isinstance(repository, GRPCRepository)
        assert repository._config == mock_app_config.service_config

    def test_get_repository_with_database_source(self, mock_app_config):
        """Test that get_repository returns PostgresRepository for 'database' source"""
        repository = get_repository(mock_app_config, SOURCE_DATABASE)
        assert isinstance(repository, PostgresRepository)
        assert repository._config == mock_app_config.database_config

    def test_get_repository_with_service_source_uppercase(self, mock_app_config):
        """Test that source parameter is case-insensitive for 'SERVICE'"""
        repository = get_repository(mock_app_config, 'SERVICE')
        assert isinstance(repository, GRPCRepository)

    def test_get_repository_with_database_source_uppercase(self, mock_app_config):
        """Test that source parameter is case-insensitive for 'DATABASE'"""
        repository = get_repository(mock_app_config, 'DATABASE')
        assert isinstance(repository, PostgresRepository)

    def test_get_repository_with_service_source_mixedcase(self, mock_app_config):
        """Test that source parameter is case-insensitive for mixed case"""
        repository = get_repository(mock_app_config, 'SeRvIcE')
        assert isinstance(repository, GRPCRepository)

    def test_get_repository_with_database_source_mixedcase(self, mock_app_config):
        """Test that source parameter is case-insensitive for mixed case"""
        repository = get_repository(mock_app_config, 'DaTaBaSe')
        assert isinstance(repository, PostgresRepository)

    def test_get_repository_with_invalid_source_defaults_to_postgres(self, mock_app_config):
        """Test that invalid source defaults to PostgresRepository"""
        repository = get_repository(mock_app_config, 'invalid')
        assert isinstance(repository, PostgresRepository)
        assert repository._config == mock_app_config.database_config

    def test_get_repository_with_empty_source_defaults_to_postgres(self, mock_app_config):
        """Test that empty source defaults to PostgresRepository"""
        repository = get_repository(mock_app_config, '')
        assert isinstance(repository, PostgresRepository)

    def test_get_repository_with_none_like_source_defaults_to_postgres(self, mock_app_config):
        """Test that various invalid sources default to PostgresRepository"""
        invalid_sources = ['unknown', 'grpc', 'db', 'rest', '12345', 'null']
        for source in invalid_sources:
            repository = get_repository(mock_app_config, source)
            assert isinstance(repository, PostgresRepository)
            assert repository._config == mock_app_config.database_config

    def test_get_repository_passes_correct_config_to_grpc(self, mock_app_config):
        """Test that service config is passed to GRPCRepository"""
        repository = get_repository(mock_app_config, SOURCE_SERVICE)
        assert repository._config == mock_app_config.service_config
        assert repository._config.host == 'localhost'
        assert repository._config.port == 50051

    def test_get_repository_passes_correct_config_to_postgres(self, mock_app_config):
        """Test that database config is passed to PostgresRepository"""
        repository = get_repository(mock_app_config, SOURCE_DATABASE)
        assert repository._config == mock_app_config.database_config
        assert repository._config.db_name == 'testdb'
        assert repository._config.user == 'testuser'

    @pytest.mark.parametrize("source,expected_type", [
        ('service', GRPCRepository),
        ('SERVICE', GRPCRepository),
        ('Service', GRPCRepository),
        ('database', PostgresRepository),
        ('DATABASE', PostgresRepository),
        ('Database', PostgresRepository),
        ('invalid', PostgresRepository),
        ('', PostgresRepository),
    ])
    def test_get_repository_with_various_sources(self, mock_app_config, source, expected_type):
        """Test get_repository with various source parameters"""
        repository = get_repository(mock_app_config, source)
        assert isinstance(repository, expected_type)
