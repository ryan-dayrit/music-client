using MusicClient.DAL;
using Xunit;

namespace MusicClient.Tests;

public class BaseRepositoryTests
{
    // Test implementation of abstract BaseRepository for testing purposes
    private class TestRepository : BaseRepository
    {
        private readonly List<Album> _albums;

        public TestRepository(List<Album> albums)
        {
            _albums = albums;
        }

        public override IEnumerable<Album> GetAlbums()
        {
            return _albums;
        }
    }

    [Fact]
    public void GetAlbums_ShouldReturnEmptyList_WhenNoAlbumsExist()
    {
        // Arrange
        var repository = new TestRepository(new List<Album>());

        // Act
        var result = repository.GetAlbums();

        // Assert
        Assert.NotNull(result);
        Assert.Empty(result);
    }

    [Fact]
    public void GetAlbums_ShouldReturnAlbums_WhenAlbumsExist()
    {
        // Arrange
        var albums = new List<Album>
        {
            new Album(1, "Album 1", "Artist 1", 10.99),
            new Album(2, "Album 2", "Artist 2", 12.99),
            new Album(3, "Album 3", "Artist 3", 15.99)
        };
        var repository = new TestRepository(albums);

        // Act
        var result = repository.GetAlbums().ToList();

        // Assert
        Assert.NotNull(result);
        Assert.Equal(3, result.Count);
        Assert.Equal(1, result[0].Id);
        Assert.Equal("Album 1", result[0].Title);
        Assert.Equal("Artist 1", result[0].Artist);
        Assert.Equal(10.99, result[0].Price);
    }

    [Fact]
    public void GetAlbums_ShouldReturnSingleAlbum_WhenOnlyOneExists()
    {
        // Arrange
        var albums = new List<Album>
        {
            new Album(1, "Single Album", "Single Artist", 9.99)
        };
        var repository = new TestRepository(albums);

        // Act
        var result = repository.GetAlbums().ToList();

        // Assert
        Assert.NotNull(result);
        Assert.Single(result);
        Assert.Equal(1, result[0].Id);
        Assert.Equal("Single Album", result[0].Title);
    }

    [Fact]
    public void GetAlbums_ShouldBeEnumerable()
    {
        // Arrange
        var albums = new List<Album>
        {
            new Album(1, "Album 1", "Artist 1", 10.99),
            new Album(2, "Album 2", "Artist 2", 12.99)
        };
        var repository = new TestRepository(albums);

        // Act
        var result = repository.GetAlbums();

        // Assert
        Assert.IsAssignableFrom<IEnumerable<Album>>(result);
        int count = 0;
        foreach (var album in result)
        {
            count++;
            Assert.NotNull(album);
        }
        Assert.Equal(2, count);
    }
}
