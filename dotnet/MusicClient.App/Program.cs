using Microsoft.Extensions.Configuration;
using MusicClient.DAL;
using System;

namespace MusicClient.App
{
    class Program
    {
        static void Main(string[] args)
        {
            var builder = new ConfigurationBuilder();
            builder.AddCommandLine(args);
            var config = builder.Build();

            string source = config["source"];
            var repository = RepositoryFactory.GetRepository(source);
            var albums = repository.GetAlbums();
            foreach (Album album in albums)
            {
                Console.WriteLine($"Id: {album.Id}, Artist: {album.Artist}, Title: {album.Title}, Price: {album.Price}");
            }
        }
    }
}