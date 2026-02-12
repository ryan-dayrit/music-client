DOTNET = dotnet
PROJECT = MusicClient.App/MusicClient.App.csproj
TEST_PROJECT = MusicClient.Tests/MusicClient.Tests.csproj

.PHONY: all run clean test

all: run

build: clean
	$(DOTNET) build 

clean:
	rm -rf MusicClient.App/bin MusicClient.App/obj
	rm -rf MusicClient.DAL/bin MusicClient.DAL/obj
	rm -rf MusicClient.Tests/bin MusicClient.Tests/obj

test:
	$(DOTNET) test $(TEST_PROJECT)

test-verbose:
	$(DOTNET) test $(TEST_PROJECT) --verbosity detailed

test-coverage:
	$(DOTNET) test $(TEST_PROJECT) --collect:"XPlat Code Coverage"

run_db_fetch: build
	$(DOTNET) run --project $(PROJECT) --source database

run_svc_fetch: build
	$(DOTNET) run --project $(PROJECT) --source service
