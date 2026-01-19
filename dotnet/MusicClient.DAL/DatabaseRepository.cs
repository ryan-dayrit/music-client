using Microsoft.Extensions.Configuration;
using Npgsql;

namespace MusicClient.DAL;

public class DatabaseRepository : BaseRepository
{
    private IConfigurationSection _config;

    public DatabaseRepository(IConfigurationSection config)
    {
        _config = config;
    }

    public override IEnumerable<Album> GetAlbums()
    {
        var connString = $"Host={_config["Host"]};Username={_config["User"]};Password={_config["Password"]};Database={_config["DBName"]}";

        var conn = new NpgsqlConnection(connString);
        conn.Open();

        var albums = new List<Album>();

        using (var cmd = new NpgsqlCommand("SELECT id, title, artist, price FROM music.albums", conn))
        {
            using (var reader = cmd.ExecuteReader())
            {
                while (reader.Read())
                {
                    albums.Add(new Album(
                        reader.GetInt32(0),
                        reader.GetString(1),
                        reader.GetString(2),
                        reader.GetDouble(3)
                    ));
                }
            }
        }

        return albums;
    }
}