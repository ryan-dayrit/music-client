# Go Music Client

Go client implementation for the shared protobuf contracts in `../proto`.

## Prerequisites

- Go 1.24+
- `protoc` in `PATH` (only required when regenerating stubs)

## Install

```bash
go mod tidy
```

## Generate protobuf stubs

```bash
make tools
make gen
```

## Build

```bash
make build
```

## Test

```bash
make test
```

## Integration test

```bash
make test-integration
```

## Run

```bash
go run ./cmd/music-client --host localhost --port 50051
```

## Notes

- Unit tests use `bufconn`; integration tests use an in-process gRPC server on an ephemeral local TCP port.
- Running the binary requires the external `music-service` gRPC service to be reachable.
