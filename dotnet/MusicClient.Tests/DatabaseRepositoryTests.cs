using Microsoft.Extensions.Configuration;
using MusicClient.DAL;
using Xunit;

namespace MusicClient.Tests;

public class DatabaseRepositoryTests
{
    [Fact]
    public void Constructor_ShouldAcceptConfigurationSection()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Database");

        // Act
        var repository = new DatabaseRepository(section);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<DatabaseRepository>(repository);
    }

    [Fact]
    public void DatabaseRepository_ShouldInheritFromBaseRepository()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Database");

        // Act
        var repository = new DatabaseRepository(section);

        // Assert
        Assert.IsAssignableFrom<BaseRepository>(repository);
    }

    [Fact]
    public void DatabaseRepository_ShouldHaveGetAlbumsMethod()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Database");
        var repository = new DatabaseRepository(section);

        // Act & Assert
        var method = repository.GetType().GetMethod("GetAlbums");
        Assert.NotNull(method);
        Assert.Equal(typeof(IEnumerable<Album>), method.ReturnType);
    }
}
