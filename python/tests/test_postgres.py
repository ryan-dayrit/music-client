import pytest
from unittest.mock import Mock, patch, MagicMock
from music.repository.postgres import PostgresRepository
from music.repository.abstract import AbstractRepository
from music.client.constants import DEFAULT_POSTGRESQL_PORT, QUERY_GET_ALBUMS


class TestPostgresRepository:
    """Test suite for the PostgresRepository class"""

    @pytest.fixture
    def mock_config(self):
        """Fixture providing mock configuration"""
        config = Mock()
        config.db_name = 'testdb'
        config.user = 'testuser'
        config.password = 'testpass'
        config.host = 'localhost'
        return config

    def test_postgres_repository_inherits_from_abstract(self):
        """Test that PostgresRepository inherits from AbstractRepository"""
        assert issubclass(PostgresRepository, AbstractRepository)

    def test_postgres_repository_initialization(self, mock_config):
        """Test that PostgresRepository initializes correctly"""
        repo = PostgresRepository(mock_config)
        assert repo._config == mock_config

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_successful_connection(self, mock_connect, mock_config):
        """Test successful database connection and query"""
        # Setup mock connection and cursor
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [
            (1, 'Album 1', 'Artist 1', 10.99),
            (2, 'Album 2', 'Artist 2', 12.99),
            (3, 'Album 3', 'Artist 3', 15.99)
        ]
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        # Execute
        repo = PostgresRepository(mock_config)
        albums = repo.get_albums()
        
        # Assert
        assert albums is not None
        assert len(albums) == 3
        assert albums[0] == (1, 'Album 1', 'Artist 1', 10.99)
        assert albums[1] == (2, 'Album 2', 'Artist 2', 12.99)
        assert albums[2] == (3, 'Album 3', 'Artist 3', 15.99)
        
        # Verify connection parameters
        mock_connect.assert_called_once_with(
            database='testdb',
            user='testuser',
            password='testpass',
            host='localhost',
            port=DEFAULT_POSTGRESQL_PORT
        )
        
        # Verify query was executed
        mock_cursor.execute.assert_called_once_with(QUERY_GET_ALBUMS)

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_empty_result(self, mock_connect, mock_config):
        """Test get_albums with empty result set"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        albums = repo.get_albums()
        
        assert albums is not None
        assert len(albums) == 0
        assert albums == []

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_handles_database_error(self, mock_connect, mock_config, capsys):
        """Test that get_albums handles database errors gracefully"""
        import psycopg2
        
        # Setup mock to raise DatabaseError
        mock_connect.side_effect = psycopg2.DatabaseError("Connection failed")
        
        # Execute
        repo = PostgresRepository(mock_config)
        result = repo.get_albums()
        
        # Assert
        assert result is None
        captured = capsys.readouterr()
        assert "Error connecting to the database" in captured.out
        assert "Connection failed" in captured.out

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_uses_default_port(self, mock_connect, mock_config):
        """Test that get_albums uses default PostgreSQL port"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        repo.get_albums()
        
        # Verify port parameter
        call_kwargs = mock_connect.call_args.kwargs
        assert call_kwargs['port'] == DEFAULT_POSTGRESQL_PORT

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_executes_correct_query(self, mock_connect, mock_config):
        """Test that get_albums executes the correct SQL query"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        repo.get_albums()
        
        # Verify the correct query was executed
        mock_cursor.execute.assert_called_once_with(QUERY_GET_ALBUMS)
        assert "SELECT id, title, artist, price FROM music.albums" in QUERY_GET_ALBUMS

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_creates_cursor(self, mock_connect, mock_config):
        """Test that get_albums creates a cursor from connection"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        repo.get_albums()
        
        # Verify cursor was created
        mock_conn.cursor.assert_called_once()

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_calls_fetchall(self, mock_connect, mock_config):
        """Test that get_albums calls fetchall to retrieve results"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [(1, 'Test', 'Artist', 9.99)]
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        albums = repo.get_albums()
        
        # Verify fetchall was called
        mock_cursor.fetchall.assert_called_once()
        assert albums == [(1, 'Test', 'Artist', 9.99)]

    @pytest.mark.parametrize("db_name,user,password,host", [
        ('production', 'admin', 'admin123', 'db.example.com'),
        ('testdb', 'testuser', 'testpass', '127.0.0.1'),
        ('dev_db', 'dev_user', 'dev_pass', 'localhost'),
    ])
    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_with_various_configs(self, mock_connect, db_name, user, password, host):
        """Test get_albums with various database configurations"""
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = []
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        config = Mock()
        config.db_name = db_name
        config.user = user
        config.password = password
        config.host = host
        
        repo = PostgresRepository(config)
        repo.get_albums()
        
        # Verify connection was called with correct parameters
        mock_connect.assert_called_once_with(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=DEFAULT_POSTGRESQL_PORT
        )

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_returns_tuples(self, mock_connect, mock_config):
        """Test that get_albums returns list of tuples"""
        mock_cursor = Mock()
        expected_data = [
            (1, 'Album 1', 'Artist 1', 10.99),
            (2, 'Album 2', 'Artist 2', 12.99)
        ]
        mock_cursor.fetchall.return_value = expected_data
        
        mock_conn = Mock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        repo = PostgresRepository(mock_config)
        albums = repo.get_albums()
        
        assert isinstance(albums, list)
        assert all(isinstance(album, tuple) for album in albums)
        assert albums == expected_data

    @patch('music.repository.postgres.psycopg2.connect')
    def test_get_albums_handles_operational_error(self, mock_connect, mock_config, capsys):
        """Test handling of OperationalError (subclass of DatabaseError)"""
        import psycopg2
        
        mock_connect.side_effect = psycopg2.OperationalError("Could not connect to server")
        
        repo = PostgresRepository(mock_config)
        result = repo.get_albums()
        
        assert result is None
        captured = capsys.readouterr()
        assert "Error connecting to the database" in captured.out
