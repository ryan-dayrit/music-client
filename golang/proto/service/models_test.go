package service

import (
	"testing"

	"google.golang.org/protobuf/proto"
)

func TestGetAlbumsResponseRoundTrip(t *testing.T) {
	t.Parallel()

	original := &GetAlbumsResponse{
		Albums: []*Album{
			{
				Id:     1,
				Title:  "Sarah Vaughan and Clifford Brown",
				Artist: "Sarah Vaughan",
				Price:  39.99,
			},
		},
	}

	bytes, err := proto.Marshal(original)
	if err != nil {
		t.Fatalf("expected marshal to succeed: %v", err)
	}

	var parsed GetAlbumsResponse
	if err := proto.Unmarshal(bytes, &parsed); err != nil {
		t.Fatalf("expected unmarshal to succeed: %v", err)
	}

	if len(parsed.GetAlbums()) != 1 {
		t.Fatalf("expected 1 album, got %d", len(parsed.GetAlbums()))
	}
	if parsed.GetAlbums()[0].GetArtist() != "Sarah Vaughan" {
		t.Fatalf("expected artist Sarah Vaughan, got %q", parsed.GetAlbums()[0].GetArtist())
	}
	if parsed.GetAlbums()[0].GetPrice() != float32(39.99) {
		t.Fatalf("expected price 39.99, got %f", parsed.GetAlbums()[0].GetPrice())
	}
}
