import sys
from unittest.mock import MagicMock, Mock, patch

import pytest
import yaml
from music.proto.gen.models_pb2 import Album, GetAlbumsResponse

from music.client.__main__ import main
from music.client.constants import DEFAULT_POSTGRESQL_PORT, QUERY_GET_ALBUMS


class TestPythonClientIntegration:
    @pytest.fixture
    def integration_config(self):
        return {
            "service": {
                "network": "tcp",
                "host": "grpc.integration.local",
                "port": 50051,
            },
            "database": {
                "driver_name": "postgres",
                "user": "integration_user",
                "db_name": "integration_db",
                "ssl_mode": "disable",
                "password": "integration_password",
                "host": "postgres.integration.local",
            },
        }

    @pytest.fixture
    def integration_config_path(self, tmp_path, integration_config):
        config_path = tmp_path / "integration-config.yaml"
        config_path.write_text(yaml.safe_dump(integration_config), encoding="utf-8")
        return config_path

    def test_main_service_source_uses_grpc_repository(
        self, integration_config_path, monkeypatch, capsys
    ):
        mock_channel_ctx = MagicMock()
        mock_stub = Mock()
        mock_stub.GetAlbumList.return_value = GetAlbumsResponse(
            albums=[
                Album(
                    id=1,
                    title="Integration Album 1",
                    artist="Integration Artist 1",
                    price=9.99,
                ),
                Album(
                    id=2,
                    title="Integration Album 2",
                    artist="Integration Artist 2",
                    price=12.5,
                ),
            ]
        )

        with patch("music.client.app.CONFIG_FILE_PATH", str(integration_config_path)):
            with patch(
                "music.repository.grpc.grpc.insecure_channel"
            ) as mock_insecure_channel:
                with patch(
                    "music.repository.grpc.MusicServiceStub", return_value=mock_stub
                ) as mock_stub_class:
                    mock_insecure_channel.return_value.__enter__.return_value = (
                        mock_channel_ctx
                    )
                    monkeypatch.setattr(
                        sys,
                        "argv",
                        ["music-client", "--source", "service"],
                    )

                    main()

        mock_insecure_channel.assert_called_once_with("grpc.integration.local:50051")
        mock_stub_class.assert_called_once_with(mock_channel_ctx)
        mock_stub.GetAlbumList.assert_called_once()

        captured = capsys.readouterr()
        assert "Integration Album 1" in captured.out
        assert "Integration Artist 2" in captured.out

    def test_main_database_source_uses_postgres_repository(
        self, integration_config_path, monkeypatch, capsys
    ):
        rows = [
            (10, "Integration DB Album 1", "DB Artist 1", 7.25),
            (11, "Integration DB Album 2", "DB Artist 2", 14.0),
        ]
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = rows
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor

        with patch("music.client.app.CONFIG_FILE_PATH", str(integration_config_path)):
            with patch(
                "music.repository.postgres.psycopg2.connect",
                return_value=mock_connection,
            ) as mock_connect:
                monkeypatch.setattr(
                    sys,
                    "argv",
                    ["music-client", "--source", "database"],
                )

                main()

        mock_connect.assert_called_once_with(
            database="integration_db",
            user="integration_user",
            password="integration_password",
            host="postgres.integration.local",
            port=DEFAULT_POSTGRESQL_PORT,
        )
        mock_cursor.execute.assert_called_once_with(QUERY_GET_ALBUMS)

        captured = capsys.readouterr()
        for row in rows:
            assert str(row) in captured.out

    def test_main_invalid_source_defaults_to_postgres_repository(
        self, integration_config_path, monkeypatch, capsys
    ):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [
            (99, "Default Path Album", "Fallback Artist", 5.5)
        ]
        mock_connection = Mock()
        mock_connection.cursor.return_value = mock_cursor

        with patch("music.client.app.CONFIG_FILE_PATH", str(integration_config_path)):
            with patch(
                "music.repository.postgres.psycopg2.connect",
                return_value=mock_connection,
            ) as mock_connect:
                with patch(
                    "music.repository.grpc.grpc.insecure_channel"
                ) as mock_insecure_channel:
                    monkeypatch.setattr(
                        sys,
                        "argv",
                        ["music-client", "--source", "unknown"],
                    )

                    main()

        mock_connect.assert_called_once()
        mock_insecure_channel.assert_not_called()
        captured = capsys.readouterr()
        assert "Default Path Album" in captured.out
