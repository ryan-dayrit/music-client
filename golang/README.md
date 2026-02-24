# Go Music Client

Go client implementation for the shared protobuf contracts in `../proto`.

## Prerequisites

- Go 1.22+
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

## Run

```bash
go run ./cmd/music-client --host localhost --port 50051
```

## Notes

- The test suite uses `bufconn` and does not require a live gRPC server.
- Running the binary requires the external `music-service` gRPC service to be reachable.
