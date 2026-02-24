package client

import (
	"context"
	"errors"
	"strings"
	"time"

	service "github.com/ryan-dayrit/music-client/golang/proto/service"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const defaultDialTimeout = 5 * time.Second

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
		grpc.WithReturnConnectionError(),
	}
	opts = append(opts, dialOptions...)

	ctx, cancel := context.WithTimeout(context.Background(), defaultDialTimeout)
	defer cancel()

	conn, err := grpc.DialContext(ctx, address, opts...)
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
		ctx = context.Background()
	}

	response, err := c.svc.GetAlbumList(ctx, &service.GetAlbumsRequest{})
	if err != nil {
		return nil, err
	}

	return response.GetAlbums(), nil
}
