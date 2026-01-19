import grpc
from music.repository.abstract import AbstractRepository
from models_pb2 import GetAlbumsRequest, GetAlbumsResponse
from service_pb2_grpc import MusicServiceStub

class GRPCRepository(AbstractRepository):
    def get_albums(self):
        with grpc.insecure_channel(f"{self._config.host}:{self._config.port}") as channel:
            stub = MusicServiceStub(channel)
            try:
                response = stub.GetAlbumList(GetAlbumsRequest())
                return response.albums
            except grpc.RpcError as e:
                print(f"Error: {e.details()}")
                return None