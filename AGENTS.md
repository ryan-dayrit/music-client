# AGENTS.md

## Cursor Cloud specific instructions

This repository contains two client applications (Python and C# .NET) that fetch music album data from either a PostgreSQL database or a gRPC service. All tests are fully mocked and do **not** require external services.

### Prerequisites (installed by update script)

- **Python 3.12+** (system-provided) with deps from `python/requirements-test.txt`
- **.NET 10 SDK** installed to `/usr/share/dotnet` (symlinked at `/usr/local/bin/dotnet`)

### Running Tests

| Project | Command | Working Directory |
|---------|---------|-------------------|
| Python  | `make test` | `python/` |
| .NET    | `dotnet test` or `make test` | `dotnet/` |

See `python/README.md` and `dotnet/README.md` for additional test commands (verbose, coverage).

### Building / Running

- **Python**: Run `make gen` (from `python/`) first to generate protobuf stubs, then `make run_db_fetch` or `make run_svc_fetch`. The `gen` target cleans generated files before regenerating.
- **.NET**: `dotnet build` (from `dotnet/`) restores NuGet packages and builds. Run with `dotnet run --project MusicClient.App/MusicClient.App.csproj --source database` (or `service`).

### Gotchas

- The Python `make gen` target runs `make clean` first, which deletes `*_pb2*.py` files and `__pycache__`. This is expected.
- `.NET` project targets `net10.0`. The SDK is installed via the official install script, not via `apt`, because Ubuntu 24.04 apt feeds don't carry .NET 10.
- Running the apps in `database` mode requires a PostgreSQL instance (not available in CI/cloud); running in `service` mode requires an external gRPC service (also not in this repo). Tests don't need either.
- Python pip packages install to `~/.local`; ensure `PATH` includes `/home/ubuntu/.local/bin` for pytest/protoc CLI tools.
