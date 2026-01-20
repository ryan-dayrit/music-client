using Microsoft.Extensions.Configuration;
using Grpc.Net.Client;
using Service;

namespace MusicClient.DAL;

public class ServiceRepository : BaseRepository
{
    private IConfigurationSection _config;

    public ServiceRepository(IConfigurationSection config)
    {
        _config = config;
    }

    public override IEnumerable<Album> GetAlbums()
    {
        var channel = GrpcChannel.ForAddress($"{_config["Network"]}://{_config["Host"]}:{_config["Port"]}");
        var client = new MusicService.MusicServiceClient(channel);

        var response = client.GetAlbumList(new GetAlbumsRequest());

        var result = new List<Album>();
        foreach (Service.Album album in response.Albums)
        {
            result.Add(new Album(
                album.Id,
                album.Title,
                album.Artist,
                album.Price
            ));
        }
        return result;
    }
}