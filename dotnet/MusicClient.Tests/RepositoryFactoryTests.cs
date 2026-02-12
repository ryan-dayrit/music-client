using Microsoft.Extensions.Configuration;
using MusicClient.DAL;
using Xunit;

namespace MusicClient.Tests;

public class RepositoryFactoryTests
{
    [Fact]
    public void GetRepository_WithServiceSource_ShouldReturnServiceRepository()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", "service" },
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }

    [Fact]
    public void GetRepository_WithDatabaseSource_ShouldReturnDatabaseRepository()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", "database" },
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<DatabaseRepository>(repository);
    }

    [Fact]
    public void GetRepository_WithDatabaseSourceUpperCase_ShouldReturnDatabaseRepository()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", "DATABASE" },
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<DatabaseRepository>(repository);
    }

    [Fact]
    public void GetRepository_WithNoSource_ShouldReturnServiceRepositoryByDefault()
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

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }

    [Fact]
    public void GetRepository_WithInvalidSource_ShouldReturnServiceRepositoryByDefault()
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", "invalid" },
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }

    [Theory]
    [InlineData("service")]
    [InlineData("Service")]
    [InlineData("SERVICE")]
    [InlineData("sErViCe")]
    public void GetRepository_WithServiceSourceCaseInsensitive_ShouldReturnServiceRepository(string source)
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", source },
            { "Service:Network", "http" },
            { "Service:Host", "localhost" },
            { "Service:Port", "50051" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<ServiceRepository>(repository);
    }

    [Theory]
    [InlineData("database")]
    [InlineData("Database")]
    [InlineData("DATABASE")]
    [InlineData("dAtAbAsE")]
    public void GetRepository_WithDatabaseSourceCaseInsensitive_ShouldReturnDatabaseRepository(string source)
    {
        // Arrange
        var configData = new Dictionary<string, string?>
        {
            { "Source", source },
            { "Database:Host", "localhost" },
            { "Database:User", "testuser" },
            { "Database:Password", "testpass" },
            { "Database:DBName", "testdb" }
        };
        var config = new ConfigurationBuilder()
            .AddInMemoryCollection(configData)
            .Build();

        // Act
        var repository = RepositoryFactory.GetRepository(config);

        // Assert
        Assert.NotNull(repository);
        Assert.IsType<DatabaseRepository>(repository);
    }
}
