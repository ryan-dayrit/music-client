# How to Run 
  * `dotnet build` 
  * `dotnet run --project ./MusicClient.App/MusicClient.App.csproj --source database`
  * `dotnet run --project ./MusicClient.App/MusicClient.App.csproj --source service`

# Running Tests
  * `make test` - Run all unit tests
  * `make test-verbose` - Run tests with detailed output
  * `make test-coverage` - Run tests with code coverage
  * `dotnet test` - Run tests directly with dotnet CLI

# Test Coverage
The test suite includes:
  * **AlbumTests** - Tests for the Album model
  * **BaseRepositoryTests** - Tests for the abstract repository
  * **DatabaseRepositoryTests** - Tests for database repository
  * **ServiceRepositoryTests** - Tests for gRPC service repository
  * **RepositoryFactoryTests** - Tests for repository factory pattern

All tests pass: **31 tests succeeded**

# Usage 
  * 2 values for the --source parameter 
    * database for querying postgres database directly 
    * service for calling the music-service gRPC service 

# dotnet install 
  * https://learn.microsoft.com/en-us/dotnet/core/install/macos

# Data Access Layer & Configurations 
  * https://kaanceliker.medium.com/part-4-deep-dive-into-the-data-access-layer-dal-and-configurations-ae94721eee2e

# Arguments 
  * https://www.google.com/search?q=how+to+process+arguments+in+dotnetcore

# dotnet CLI 
  * https://www.google.com/search?q=adding+a+library+project+in+dotnet+core

# static functions 
  * https://www.google.com/search?q=static+functions+in+dotnetcore

# abstract classes 
  * https://www.google.com/search?q=how+to+implement+an+abstract+class+in+dotnetcore

# return types 
  * https://www.google.com/search?q=return+type+in+dotnetcore+c%23+methods

# constructors 
  * https://www.google.com/search?q=constructor+in+dotnetcore+c%23

# switch statements 
  * https://www.google.com/search?q=switch+statement+for+strings+in+dotnetcore+c%23

# properties 
  * https://www.google.com/search?q=properties+in+c%23+dotnet

# returning collections 
  * https://www.google.com/search?q=returning+a+collection+in+c%23+dotnetcore

# foreach 
  * https://www.google.com/search?q=foreach+c%23+dotnetcore

# string interpolation 
  * https://www.google.com/search?q=string+interpolation+c%23+dotnetcore

# Accessing PostgreSQL
  * https://www.npgsql.org/