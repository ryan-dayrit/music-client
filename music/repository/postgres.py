from music.repository.abstract import AbstractRepository

class PostgresRepository(AbstractRepository):
    def get_album_list(self):
        print("getting album list from postgres database")