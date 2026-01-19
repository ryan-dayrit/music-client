using Microsoft.Extensions.Configuration;

namespace MusicClient.DAL;

public class RepositoryFactory
{
    public static BaseRepository GetRepository(IConfiguration config)
    { 
        BaseRepository repository;
        var source = config["Source"] ?? "service";
        switch(source.ToLower())
        {
            case "database":
                repository = new DatabaseRepository(config.GetSection("Database"));
                break;
            case "service":
            default:
                repository = new ServiceRepository(config.GetSection("Service")); 
                break;
        }
        return repository;     
    }
}
