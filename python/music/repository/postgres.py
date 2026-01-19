import psycopg2

from music.repository.abstract import AbstractRepository
from music.client.constants import (
    DEFAULT_POSTGRESQL_PORT, 
    QUERY_GET_ALBUMS
)

class PostgresRepository(AbstractRepository):
    def get_albums(self):
        try:
            conn = psycopg2.connect(
                database=self._config.db_name,
                user=self._config.user,
                password=self._config.password,
                host=self._config.host,
                port=DEFAULT_POSTGRESQL_PORT 
            )
        except psycopg2.DatabaseError as e:
            print(f"Error connecting to the database: {e}")
            return None
        
        cur = conn.cursor()
        cur.execute(QUERY_GET_ALBUMS)
        return cur.fetchall()
