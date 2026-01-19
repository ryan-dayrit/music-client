using Microsoft.Extensions.Configuration;
using MusicClient.DAL;
using System;

namespace MusicClient.App
{
    class Program
    {
        static void Main(string[] args)
        {
            var configBuilder = new ConfigurationBuilder();
            configBuilder.AddCommandLine(args);
            configBuilder.AddJsonFile("appsettings.json");
            var config = configBuilder.Build();

            var repository = RepositoryFactory.GetRepository(config);
            var albums = repository.GetAlbums();
            foreach (Album album in albums)
            {
                Console.WriteLine($"Id: {album.Id}, Artist: {album.Artist}, Title: {album.Title}, Price: {album.Price}");
            }
        }
    }
}