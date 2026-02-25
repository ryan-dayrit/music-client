package client

import (
	"context"
	"errors"
	"strings"

	service "github.com/ryan-dayrit/music-client/golang/proto/service"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

// Client wraps the generated protobuf service client.
type Client struct {
	conn *grpc.ClientConn
	svc  service.MusicServiceClient
}

// New creates a gRPC client connection to the music service.
func New(address string, dialOptions ...grpc.DialOption) (*Client, error) {
	if strings.TrimSpace(address) == "" {
		return nil, errors.New("address must not be empty")
	}

	opts := []grpc.DialOption{
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	}
	opts = append(opts, dialOptions...)

	conn, err := grpc.NewClient(address, opts...)
	if err != nil {
		return nil, err
	}

	return &Client{
		conn: conn,
		svc:  service.NewMusicServiceClient(conn),
	}, nil
}

// Close closes the underlying gRPC connection.
func (c *Client) Close() error {
	if c == nil || c.conn == nil {
		return nil
	}
	return c.conn.Close()
}

// GetAlbumList fetches albums from the music service.
func (c *Client) GetAlbumList(ctx context.Context) ([]*service.Album, error) {
	if c == nil || c.svc == nil {
		return nil, errors.New("client is not initialized")
	}
	if ctx == nil {
		return nil, errors.New("context must not be nil")
	}

	response, err := c.svc.GetAlbumList(ctx, &service.GetAlbumsRequest{})
	if err != nil {
		return nil, err
	}

	return response.GetAlbums(), nil
}
