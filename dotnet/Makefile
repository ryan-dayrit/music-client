DOTNET = dotnet
PROJECT = MusicClient.App/MusicClient.App.csproj

.PHONY: all run clean

all: run

build: clean
	$(DOTNET) build 

clean:
	rm -rf MusicClient.App/bin MusicClient.App/obj
	rm -rf MusicClient.DAL/bin MusicClient.DAL/obj

run_db_fetch: build
	$(DOTNET) run --project $(PROJECT) --source database

run_svc_fetch: build
	$(DOTNET) run --project $(PROJECT) --source service
