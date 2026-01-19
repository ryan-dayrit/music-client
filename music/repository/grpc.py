from music.repository.abstract import AbstractRepository

class GRPCRepository(AbstractRepository):
    def get_album_list(self):
        print("getting album list from gRPC service")