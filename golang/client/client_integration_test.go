package client_test

import (
	"context"
	"net"
	"strings"
	"testing"
	"time"

	clientpkg "github.com/ryan-dayrit/music-client/golang/client"
	service "github.com/ryan-dayrit/music-client/golang/proto/service"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type integrationMusicService struct {
	service.UnimplementedMusicServiceServer
	response *service.GetAlbumsResponse
	err      error
	delay    time.Duration
}

func (s *integrationMusicService) GetAlbumList(ctx context.Context, _ *service.GetAlbumsRequest) (*service.GetAlbumsResponse, error) {
	if s.delay > 0 {
		select {
		case <-time.After(s.delay):
		case <-ctx.Done():
			return nil, status.Error(codes.DeadlineExceeded, "request deadline exceeded")
		}
	}

	if s.err != nil {
		return nil, s.err
	}

	if s.response == nil {
		return &service.GetAlbumsResponse{}, nil
	}

	return s.response, nil
}

func startIntegrationServer(t *testing.T, srv service.MusicServiceServer) string {
	t.Helper()

	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatalf("failed to start listener: %v", err)
	}

	grpcServer := grpc.NewServer()
	service.RegisterMusicServiceServer(grpcServer, srv)

	go func() {
		_ = grpcServer.Serve(listener)
	}()

	t.Cleanup(func() {
		grpcServer.Stop()
		_ = listener.Close()
	})

	return listener.Addr().String()
}

func TestIntegrationClientFetchesAlbumsOverGRPC(t *testing.T) {
	t.Parallel()

	address := startIntegrationServer(t, &integrationMusicService{
		response: &service.GetAlbumsResponse{
			Albums: []*service.Album{
				{Id: 1, Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
				{Id: 2, Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
			},
		},
	})

	c, err := clientpkg.New(address)
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	albums, err := c.GetAlbumList(ctx)
	if err != nil {
		t.Fatalf("expected successful GetAlbumList call, got: %v", err)
	}

	if len(albums) != 2 {
		t.Fatalf("expected 2 albums, got %d", len(albums))
	}
	if albums[0].GetTitle() != "Blue Train" {
		t.Fatalf("unexpected first album title: %q", albums[0].GetTitle())
	}
	if albums[1].GetArtist() != "Gerry Mulligan" {
		t.Fatalf("unexpected second album artist: %q", albums[1].GetArtist())
	}
}

func TestIntegrationClientPropagatesServiceError(t *testing.T) {
	t.Parallel()

	address := startIntegrationServer(t, &integrationMusicService{
		err: status.Error(codes.Unavailable, "service unavailable"),
	})

	c, err := clientpkg.New(address)
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	albums, err := c.GetAlbumList(ctx)
	if err == nil {
		t.Fatal("expected error from service")
	}
	if albums != nil {
		t.Fatal("expected nil albums when service returns an error")
	}

	statusErr, ok := status.FromError(err)
	if !ok {
		t.Fatalf("expected gRPC status error, got: %v", err)
	}
	if statusErr.Code() != codes.Unavailable {
		t.Fatalf("expected status code %s, got %s", codes.Unavailable, statusErr.Code())
	}
	if !strings.Contains(err.Error(), "service unavailable") {
		t.Fatalf("unexpected error message: %v", err)
	}
}

func TestIntegrationClientRespectsContextDeadline(t *testing.T) {
	t.Parallel()

	address := startIntegrationServer(t, &integrationMusicService{
		delay:    250 * time.Millisecond,
		response: &service.GetAlbumsResponse{Albums: []*service.Album{}},
	})

	c, err := clientpkg.New(address)
	if err != nil {
		t.Fatalf("unexpected dial error: %v", err)
	}
	t.Cleanup(func() {
		_ = c.Close()
	})

	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Millisecond)
	defer cancel()

	albums, err := c.GetAlbumList(ctx)
	if err == nil {
		t.Fatal("expected deadline exceeded error")
	}
	if albums != nil {
		t.Fatal("expected nil albums when request times out")
	}

	statusErr, ok := status.FromError(err)
	if !ok {
		t.Fatalf("expected gRPC status error, got: %v", err)
	}
	if statusErr.Code() != codes.DeadlineExceeded {
		t.Fatalf("expected status code %s, got %s", codes.DeadlineExceeded, statusErr.Code())
	}
}
