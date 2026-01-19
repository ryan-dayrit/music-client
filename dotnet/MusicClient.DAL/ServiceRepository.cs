namespace MusicClient.DAL;

public class ServiceRepository : BaseRepository
{
    public ServiceRepository() 
    {
    }

    public override IEnumerable<Album> GetAlbums()
    {
        return new List<Album>
        {
            new Album(1, "Jeru", "Gerry Mulligan", 17.99),
            new Album(2, "Sarah Vaughan", "Sarah Vaughan", 34.98)
        };
    }
}