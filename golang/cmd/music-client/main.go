package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"time"

	"github.com/ryan-dayrit/music-client/golang/client"
)

func main() {
	host := flag.String("host", "localhost", "gRPC service host")
	port := flag.Int("port", 50051, "gRPC service port")
	timeout := flag.Duration("timeout", 5*time.Second, "request timeout")
	flag.Parse()

	address := fmt.Sprintf("%s:%d", *host, *port)
	c, err := client.New(address)
	if err != nil {
		log.Fatalf("failed to connect to service: %v", err)
	}
	defer func() {
		if closeErr := c.Close(); closeErr != nil {
			log.Printf("failed to close client: %v", closeErr)
		}
	}()

	ctx, cancel := context.WithTimeout(context.Background(), *timeout)
	defer cancel()

	albums, err := c.GetAlbumList(ctx)
	if err != nil {
		log.Fatalf("GetAlbumList failed: %v", err)
	}

	for _, album := range albums {
		fmt.Printf("Id: %d, Artist: %s, Title: %s, Price: %.2f\n", album.GetId(), album.GetArtist(), album.GetTitle(), album.GetPrice())
	}
}
