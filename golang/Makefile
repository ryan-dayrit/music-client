GO = go
MODULE = github.com/ryan-dayrit/music-client/golang
PROTO_DIR = ../proto
PROTO_FILES = $(PROTO_DIR)/models.proto $(PROTO_DIR)/service.proto

.PHONY: test build run gen tools

test:
	$(GO) test ./...

build:
	$(GO) build ./...

run:
	$(GO) run ./cmd/music-client --host localhost --port 50051

tools:
	$(GO) install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	$(GO) install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

gen:
	@echo "Generating protobuf stubs (requires protoc in PATH)..."
	PATH="$$(go env GOPATH)/bin:$$PATH" protoc -I $(PROTO_DIR) \
		--go_out=. \
		--go_opt=module=$(MODULE) \
		--go_opt=Mmodels.proto=$(MODULE)/proto/service \
		--go_opt=Mservice.proto=$(MODULE)/proto/service \
		--go-grpc_out=. \
		--go-grpc_opt=module=$(MODULE) \
		--go-grpc_opt=Mmodels.proto=$(MODULE)/proto/service \
		--go-grpc_opt=Mservice.proto=$(MODULE)/proto/service \
		$(PROTO_FILES)
