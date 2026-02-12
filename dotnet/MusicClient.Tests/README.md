# MusicClient.Tests

Unit tests for the MusicClient .NET application.

## Test Coverage

This test suite provides comprehensive coverage for the MusicClient application:

### AlbumTests
- Tests the `Album` model class
- Validates constructor and property behavior
- Tests various data scenarios

### BaseRepositoryTests
- Tests the abstract `BaseRepository` class
- Validates inheritance and contract implementation
- Tests enumerable behavior

### DatabaseRepositoryTests
- Tests the `DatabaseRepository` class
- Validates configuration handling
- Tests inheritance from `BaseRepository`

### ServiceRepositoryTests
- Tests the `ServiceRepository` class
- Validates gRPC service configuration
- Tests inheritance from `BaseRepository`
- Tests various configuration scenarios

### RepositoryFactoryTests
- Tests the `RepositoryFactory` class
- Validates factory pattern implementation
- Tests source selection logic (service vs database)
- Tests case-insensitivity
- Tests default behavior

## Running Tests

### Run all tests
```bash
dotnet test
```

### Run tests with detailed output
```bash
dotnet test --verbosity detailed
```

### Run tests with coverage
```bash
dotnet test --collect:"XPlat Code Coverage"
```

### Run specific test class
```bash
dotnet test --filter "FullyQualifiedName~AlbumTests"
```

### Run specific test method
```bash
dotnet test --filter "FullyQualifiedName~AlbumTests.Album_Constructor_ShouldSetPropertiesCorrectly"
```

## Test Framework

- **xUnit**: Testing framework
- **Moq**: Mocking library (for future integration tests)
- **Microsoft.Extensions.Configuration**: Configuration testing

## Notes

- The `DatabaseRepositoryTests` and `ServiceRepositoryTests` test the class structure and configuration handling
- Actual database and gRPC service integration tests would require test databases or mock servers
- The factory tests validate the factory pattern and configuration-based repository selection
