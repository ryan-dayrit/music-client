from music.client.constants import (
    SOURCE_SERVICE,
    SOURCE_DATABASE,
) 
from music.repository.postgres import PostgresRepository
from music.repository.grpc import GRPCRepository

def get_repository(config, source):
    if source.lower() == SOURCE_SERVICE:
        return GRPCRepository(config.service_config)
    elif source.lower() == SOURCE_DATABASE:
        return PostgresRepository(config.database_config)
    else:
        return PostgresRepository(config.database_config)
