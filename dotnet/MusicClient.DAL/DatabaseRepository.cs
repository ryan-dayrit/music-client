namespace MusicClient.DAL;

public class DatabaseRepository : BaseRepository
{
    public DatabaseRepository() 
    {
    }

    public override IEnumerable<Album> GetAlbums()
    {
        return new List<Album>
        {
            new Album(3, "Blue Train", "John Coltrane", 56.99),
            new Album(4, "Giant Steps", "John Coltrane", 63.99),
        };
    }
}