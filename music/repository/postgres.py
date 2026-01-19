import psycopg2

from music.repository.abstract import AbstractRepository
from music.client.constants import DEFAULT_POSTGRESQL_PORT

class PostgresRepository(AbstractRepository):
    def get_album_list(self):
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
            conn = None
        
        if conn:
            cur = conn.cursor()
        
        cur.execute("SELECT id, title, artist, price FROM music.albums;")
        records = cur.fetchall()
        for row in records:
            print(row)