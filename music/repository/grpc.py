from music.repository.abstract import AbstractRepository

class GRPCRepository(AbstractRepository):
    def get_album_list(self):
        print(f"getting album list from gRPC service @ {self._config.host}:{self._config.port}")