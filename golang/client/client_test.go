package client

import (
	"context"
	"net"
	"strings"
	"testing"

	service "github.com/ryan-dayrit/music-client/golang/proto/service"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"
)

const bufConnSize = 1024 * 1024

type testMusicService struct {
	service.UnimplementedMusicServiceServer
	response *service.GetAlbumsResponse
	err      error
}

func (s *testMusicService) GetAlbumList(context.Context, *service.GetAlbumsRequest) (*service.GetAlbumsResponse, error) {
	if s.err != nil {
		return nil, s.err
	}
	return s.response, nil
}

func setupBufConnServer(t *testing.T, srv service.MusicServiceServer) *bufconn.Listener {
	t.Helper()

	listener := bufconn.Listen(bufConnSize)
	server := grpc.NewServer()
	service.RegisterMusicServiceServer(server, srv)

	go func() {
		_ = server.Serve(listener)
	}()

	t.Cleanup(server.Stop)
	t.Cleanup(func() {
		_ = listener.Close()
	})

	return listener
}

func TestNewReturnsErrorWhenAddressIsEmpty(t *testing.T) {
	t.Parallel()

	_, err := New("   ")
	if err == nil {
		t.Fatal("expected error for empty address")
	}
}

func TestGetAlbumListReturnsErrorForNilClient(t *testing.T) {
	t.Parallel()

	var c *Client
	albums, err := c.GetAlbumList(context.Background())
	if err == nil {
		t.Fatal("expected error for nil client")
	}
	if err.Error() != "client is not initialized" {
		t.Fatalf("unexpected error message: %v", err)
	}
	if albums != nil {
		t.Fatal("expected nil albums for nil client")
	}
}

func TestGetAlbumListReturnsErrorForNilContext(t *testing.T) {
	t.Parallel()

	listener := setupBufConnServer(t, &testMusicService{
		response: &service.GetAlbumsResponse{},
	})

	dialer := func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}

	c, err := New("bufnet", grpc.WithContextDialer(dialer))
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	albums, err := c.GetAlbumList(nil) //nolint:staticcheck
	if err == nil {
		t.Fatal("expected error for nil context")
	}
	if err.Error() != "context must not be nil" {
		t.Fatalf("unexpected error message: %v", err)
	}
	if albums != nil {
		t.Fatal("expected nil albums for nil context")
	}
}

func TestGetAlbumListReturnsAlbumsFromService(t *testing.T) {
	t.Parallel()

	listener := setupBufConnServer(t, &testMusicService{
		response: &service.GetAlbumsResponse{
			Albums: []*service.Album{
				{Id: 1, Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
				{Id: 2, Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
			},
		},
	})

	dialer := func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}

	c, err := New("passthrough:///bufnet", grpc.WithContextDialer(dialer))
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	albums, err := c.GetAlbumList(context.Background())
	if err != nil {
		t.Fatalf("expected successful GetAlbumList call, got: %v", err)
	}

	if len(albums) != 2 {
		t.Fatalf("expected 2 albums, got %d", len(albums))
	}
	if albums[0].GetTitle() != "Blue Train" {
		t.Fatalf("expected first album title to be Blue Train, got %q", albums[0].GetTitle())
	}
	if albums[1].GetArtist() != "Gerry Mulligan" {
		t.Fatalf("expected second album artist to be Gerry Mulligan, got %q", albums[1].GetArtist())
	}
}

func TestGetAlbumListReturnsServiceError(t *testing.T) {
	t.Parallel()

	listener := setupBufConnServer(t, &testMusicService{
		err: status.Error(codes.Unavailable, "service unavailable"),
	})

	dialer := func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}

	c, err := New("passthrough:///bufnet", grpc.WithContextDialer(dialer))
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	albums, err := c.GetAlbumList(context.Background())
	if err == nil {
		t.Fatal("expected error from service")
	}
	if albums != nil {
		t.Fatal("expected nil albums when service returns an error")
	}
	if !strings.Contains(err.Error(), "service unavailable") {
		t.Fatalf("unexpected error message: %v", err)
	}
}

func TestCloseNilClientReturnsNil(t *testing.T) {
	t.Parallel()

	var c *Client
	if err := c.Close(); err != nil {
		t.Fatalf("expected nil error for nil client, got: %v", err)
	}
}

func TestCloseNilConnReturnsNil(t *testing.T) {
	t.Parallel()

	c := &Client{}
	if err := c.Close(); err != nil {
		t.Fatalf("expected nil error for nil conn, got: %v", err)
	}
}

func TestCloseSucceeds(t *testing.T) {
	t.Parallel()

	listener := setupBufConnServer(t, &testMusicService{})

	dialer := func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}

	c, err := New("bufnet", grpc.WithContextDialer(dialer))
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}

	if err := c.Close(); err != nil {
		t.Fatalf("expected Close() to succeed, got: %v", err)
	}
}

func TestCloseAlreadyClosedReturnsError(t *testing.T) {
	t.Parallel()

	listener := setupBufConnServer(t, &testMusicService{})

	dialer := func(context.Context, string) (net.Conn, error) {
		return listener.Dial()
	}

	c, err := New("bufnet", grpc.WithContextDialer(dialer))
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}

	if err := c.Close(); err != nil {
		t.Fatalf("expected first Close() to succeed, got: %v", err)
	}

	if err := c.Close(); err == nil {
		t.Fatal("expected error on second Close() of an already-closed connection")
	}
}
