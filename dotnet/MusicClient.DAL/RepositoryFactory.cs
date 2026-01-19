namespace MusicClient.DAL;

public class RepositoryFactory
{
    public static BaseRepository GetRepository(string source)
    { 
        BaseRepository repository;
        switch(source)
        {
            case "database":
                repository = new DatabaseRepository();
                break;
            case "service":
                repository =  new ServiceRepository();
                break;
            default:
                repository = new ServiceRepository(); 
                break;
        }
        return repository;     
    }
}
