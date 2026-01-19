namespace MusicClient.DAL;

public abstract class BaseRepository
{
    public abstract IEnumerable<Album> GetAlbums();
}