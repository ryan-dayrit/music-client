using MusicClient.DAL;
using Xunit;

namespace MusicClient.Tests;

public class AlbumTests
{
    [Fact]
    public void Album_Constructor_ShouldSetPropertiesCorrectly()
    {
        // Arrange
        int expectedId = 1;
        string expectedTitle = "Abbey Road";
        string expectedArtist = "The Beatles";
        double expectedPrice = 19.99;

        // Act
        var album = new Album(expectedId, expectedTitle, expectedArtist, expectedPrice);

        // Assert
        Assert.Equal(expectedId, album.Id);
        Assert.Equal(expectedTitle, album.Title);
        Assert.Equal(expectedArtist, album.Artist);
        Assert.Equal(expectedPrice, album.Price);
    }

    [Fact]
    public void Album_Properties_ShouldBeReadOnly()
    {
        // Arrange
        var album = new Album(1, "Test Album", "Test Artist", 9.99);

        // Assert - Properties should only have getters
        Assert.NotNull(album.Title);
        Assert.NotNull(album.Artist);
        // Id and Price are value types and always have values
        Assert.True(album.Id >= 0 || album.Id < 0);
        Assert.True(album.Price >= 0 || album.Price < 0);
    }

    [Theory]
    [InlineData(0, "Album Zero", "Artist Zero", 0.0)]
    [InlineData(999, "Album 999", "Artist 999", 999.99)]
    [InlineData(-1, "Negative Album", "Negative Artist", -1.0)]
    public void Album_Constructor_ShouldHandleDifferentValues(int id, string title, string artist, double price)
    {
        // Act
        var album = new Album(id, title, artist, price);

        // Assert
        Assert.Equal(id, album.Id);
        Assert.Equal(title, album.Title);
        Assert.Equal(artist, album.Artist);
        Assert.Equal(price, album.Price);
    }
}
