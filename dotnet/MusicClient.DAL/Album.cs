namespace MusicClient.DAL;

public class Album 
{
    public int Id { get; }
    public string Title { get; }
    public string Artist { get; }
    public double Price { get; } 

    public Album(int id, string title, string artist, double price)
    {
        Id = id;
        Title = title; 
        Artist = artist; 
        Price = price;
    }
}