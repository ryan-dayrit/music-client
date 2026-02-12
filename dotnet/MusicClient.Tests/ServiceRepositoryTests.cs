using Microsoft.Extensions.Configuration;
using MusicClient.DAL;
using Xunit;

namespace MusicClient.Tests;

public class ServiceRepositoryTests
{
    [Fact]
    public void Constructor_ShouldAcceptConfigurationSection()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Service");

        // Act
        var repository = new ServiceRepository(section);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }

    [Fact]
    public void ServiceRepository_ShouldInheritFromBaseRepository()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Service");

        // Act
        var repository = new ServiceRepository(section);

        // Assert
        Assert.IsAssignableFrom<BaseRepository>(repository);
    }

    [Fact]
    public void ServiceRepository_ShouldHaveGetAlbumsMethod()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Service");
        var repository = new ServiceRepository(section);

        // Act & Assert
        var method = repository.GetType().GetMethod("GetAlbums");
        Assert.NotNull(method);
        Assert.Equal(typeof(IEnumerable<Album>), method.ReturnType);
    }

    [Theory]
    [InlineData("http", "localhost", "50051")]
    [InlineData("https", "example.com", "443")]
    [InlineData("http", "127.0.0.1", "8080")]
    public void Constructor_ShouldAcceptDifferentConfigurations(string network, string host, string port)
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Service:Network", network },
            { "Service:Host", host },
            { "Service:Port", port }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();
        var section = config.GetSection("Service");

        // Act
        var repository = new ServiceRepository(section);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }
}
