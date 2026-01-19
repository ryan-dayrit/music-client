using Microsoft.Extensions.Configuration;

namespace MusicClient.DAL;

public class ServiceRepository : BaseRepository
{
    private IConfigurationSection _config;

    public ServiceRepository(IConfigurationSection config)
    {
        _config = config;
        Console.WriteLine($"Network: {_config["Network"]}, Host: {_config["Host"]}, Port: {_config["Port"]}");
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