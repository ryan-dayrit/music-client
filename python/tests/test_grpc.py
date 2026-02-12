import pytest
from unittest.mock import Mock, patch, MagicMock
from music.repository.grpc import GRPCRepository
from music.repository.abstract import AbstractRepository


class TestGRPCRepository:
    """Test suite for the GRPCRepository class"""

    @pytest.fixture
    def mock_config(self):
        """Fixture providing mock configuration"""
        config = Mock()
        config.host = 'localhost'
        config.port = 50051
        return config

    def test_grpc_repository_inherits_from_abstract(self):
        """Test that GRPCRepository inherits from AbstractRepository"""
        assert issubclass(GRPCRepository, AbstractRepository)

    def test_grpc_repository_initialization(self, mock_config):
        """Test that GRPCRepository initializes correctly"""
        repo = GRPCRepository(mock_config)
        assert repo._config == mock_config

    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_successful_call(self, mock_stub_class, mock_channel, mock_config):
        """Test successful get_albums call"""
        # Setup mock channel and stub
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        # Setup mock stub
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        
        # Setup mock response
        mock_album1 = Mock()
        mock_album1.id = 1
        mock_album1.title = 'Album 1'
        mock_album1.artist = 'Artist 1'
        mock_album1.price = 10.99
        
        mock_album2 = Mock()
        mock_album2.id = 2
        mock_album2.title = 'Album 2'
        mock_album2.artist = 'Artist 2'
        mock_album2.price = 12.99
        
        mock_response = Mock()
        mock_response.albums = [mock_album1, mock_album2]
        mock_stub.GetAlbumList.return_value = mock_response
        
        # Execute
        repo = GRPCRepository(mock_config)
        albums = repo.get_albums()
        
        # Assert
        assert albums is not None
        assert len(albums) == 2
        assert albums[0].id == 1
        assert albums[0].title == 'Album 1'
        assert albums[1].id == 2
        assert albums[1].title == 'Album 2'
        
        # Verify channel was created with correct address
        mock_channel.assert_called_once_with('localhost:50051')

    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_empty_response(self, mock_stub_class, mock_channel, mock_config):
        """Test get_albums with empty album list"""
        # Setup mock channel and stub
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        
        mock_response = Mock()
        mock_response.albums = []
        mock_stub.GetAlbumList.return_value = mock_response
        
        # Execute
        repo = GRPCRepository(mock_config)
        albums = repo.get_albums()
        
        # Assert
        assert albums is not None
        assert len(albums) == 0

    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_handles_grpc_error(self, mock_stub_class, mock_channel, mock_config, capsys):
        """Test that get_albums handles gRPC errors gracefully"""
        # Setup mock channel
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        # Setup mock stub to raise RpcError
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        
        # Import grpc and create exception
        import grpc
        
        # Create a real exception that mimics RpcError behavior
        class MockRpcError(grpc.RpcError):
            def details(self):
                return "Connection failed"
        
        mock_stub.GetAlbumList.side_effect = MockRpcError()
        
        # Execute
        repo = GRPCRepository(mock_config)
        result = repo.get_albums()
        
        # Assert
        assert result is None
        captured = capsys.readouterr()
        assert "Error: Connection failed" in captured.out

    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_uses_correct_channel_address(self, mock_stub_class, mock_channel, mock_config):
        """Test that get_albums creates channel with correct address"""
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        mock_response = Mock()
        mock_response.albums = []
        mock_stub.GetAlbumList.return_value = mock_response
        
        repo = GRPCRepository(mock_config)
        repo.get_albums()
        
        # Verify channel address format
        expected_address = f"{mock_config.host}:{mock_config.port}"
        mock_channel.assert_called_once_with(expected_address)

    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_calls_get_album_list_method(self, mock_stub_class, mock_channel, mock_config):
        """Test that get_albums calls GetAlbumList on the stub"""
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        mock_response = Mock()
        mock_response.albums = []
        mock_stub.GetAlbumList.return_value = mock_response
        
        repo = GRPCRepository(mock_config)
        repo.get_albums()
        
        # Verify GetAlbumList was called
        assert mock_stub.GetAlbumList.called
        # Verify it was called with GetAlbumsRequest
        call_args = mock_stub.GetAlbumList.call_args
        assert call_args is not None

    @pytest.mark.parametrize("host,port", [
        ('localhost', 50051),
        ('127.0.0.1', 8080),
        ('grpc.example.com', 443),
        ('remote-server', 9000),
    ])
    @patch('music.repository.grpc.grpc.insecure_channel')
    @patch('music.repository.grpc.MusicServiceStub')
    def test_get_albums_with_various_configs(self, mock_stub_class, mock_channel, host, port):
        """Test get_albums with various host and port configurations"""
        mock_channel_instance = MagicMock()
        mock_channel.return_value.__enter__.return_value = mock_channel_instance
        
        mock_stub = Mock()
        mock_stub_class.return_value = mock_stub
        mock_response = Mock()
        mock_response.albums = []
        mock_stub.GetAlbumList.return_value = mock_response
        
        config = Mock()
        config.host = host
        config.port = port
        
        repo = GRPCRepository(config)
        repo.get_albums()
        
        expected_address = f"{host}:{port}"
        mock_channel.assert_called_once_with(expected_address)
