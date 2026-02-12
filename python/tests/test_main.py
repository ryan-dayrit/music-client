import pytest
from unittest.mock import patch, Mock
from music.client.__main__ import main


class TestMain:
    """Test suite for the main entry point"""

    @patch('music.client.__main__.App')
    @patch('music.client.__main__.argparse.ArgumentParser.parse_args')
    def test_main_calls_app_run(self, mock_parse_args, mock_app_class):
        """Test that main creates App and calls run method"""
        # Setup mocks
        mock_args = Mock()
        mock_args.source = 'service'
        mock_parse_args.return_value = mock_args
        
        mock_app_instance = Mock()
        mock_app_class.return_value = mock_app_instance
        
        # Execute
        main()
        
        # Assert
        mock_app_class.assert_called_once()
        mock_app_instance.run.assert_called_once_with('service')

    @patch('music.client.__main__.App')
    @patch('music.client.__main__.argparse.ArgumentParser.parse_args')
    def test_main_passes_source_argument_to_app(self, mock_parse_args, mock_app_class):
        """Test that main passes source argument to App.run"""
        # Setup mocks
        mock_args = Mock()
        mock_args.source = 'database'
        mock_parse_args.return_value = mock_args
        
        mock_app_instance = Mock()
        mock_app_class.return_value = mock_app_instance
        
        # Execute
        main()
        
        # Assert
        mock_app_instance.run.assert_called_once_with('database')

    @patch('music.client.__main__.App')
    @patch('music.client.__main__.argparse.ArgumentParser.parse_args')
    def test_main_with_none_source(self, mock_parse_args, mock_app_class):
        """Test main with None as source argument"""
        mock_args = Mock()
        mock_args.source = None
        mock_parse_args.return_value = mock_args
        
        mock_app_instance = Mock()
        mock_app_class.return_value = mock_app_instance
        
        main()
        
        mock_app_instance.run.assert_called_once_with(None)

    @pytest.mark.parametrize("source", [
        'service',
        'database',
        'SERVICE',
        'DATABASE',
        'invalid',
        '',
    ])
    @patch('music.client.__main__.App')
    @patch('music.client.__main__.argparse.ArgumentParser.parse_args')
    def test_main_with_various_sources(self, mock_parse_args, mock_app_class, source):
        """Test main with various source values"""
        mock_args = Mock()
        mock_args.source = source
        mock_parse_args.return_value = mock_args
        
        mock_app_instance = Mock()
        mock_app_class.return_value = mock_app_instance
        
        main()
        
        mock_app_instance.run.assert_called_once_with(source)
