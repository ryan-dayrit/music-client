# Music Client Python Tests

Comprehensive unit test suite for the Python Music Client application.

## Test Coverage

This test suite provides comprehensive coverage for all Python modules:

### Test Files

1. **test_app.py** - Tests for the main App class
   - Configuration file reading
   - YAML parsing error handling
   - File not found handling
   - Repository integration
   - Album output

2. **test_config.py** - Tests for configuration classes
   - Config base class
   - ServiceConfig properties
   - DatabaseConfig properties
   - AppConfig initialization

3. **test_constants.py** - Tests for constants module
   - All constant values
   - Type checking
   - Immutability

4. **test_abstract.py** - Tests for AbstractRepository
   - Abstract class behavior
   - Interface enforcement
   - Concrete implementations

5. **test_factory.py** - Tests for repository factory
   - Service repository creation
   - Database repository creation
   - Source selection logic
   - Case-insensitivity
   - Default behavior

6. **test_grpc.py** - Tests for GRPCRepository
   - gRPC channel creation
   - Service stub calls
   - Error handling
   - Configuration usage

7. **test_postgres.py** - Tests for PostgresRepository
   - Database connection
   - Query execution
   - Error handling
   - Configuration usage

8. **test_main.py** - Tests for main entry point
   - Argument parsing
   - App instantiation
   - Source parameter handling

## Installation

Install test dependencies:

```bash
pip install -r requirements-test.txt
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run with coverage report
```bash
pytest --cov=music --cov-report=term-missing
```

### Run with HTML coverage report
```bash
pytest --cov=music --cov-report=html
open htmlcov/index.html
```

### Run specific test file
```bash
pytest tests/test_app.py
```

### Run specific test class
```bash
pytest tests/test_config.py::TestConfig
```

### Run specific test method
```bash
pytest tests/test_app.py::TestApp::test_app_init_reads_config_file
```

### Run with verbose output
```bash
pytest -v
```

### Run with very verbose output
```bash
pytest -vv
```

## Test Configuration

The test suite uses `pytest.ini` for configuration:
- Test discovery patterns
- Coverage settings
- Output formatting

## Dependencies

- **pytest** (>=8.0.0) - Testing framework
- **pytest-cov** (>=4.1.0) - Coverage plugin
- **pytest-mock** (>=3.12.0) - Mocking fixtures
- **pyyaml** (>=6.0) - YAML parsing
- **psycopg2-binary** (>=2.9.9) - PostgreSQL adapter
- **grpcio** (>=1.60.0) - gRPC framework

## Test Structure

```
tests/
├── __init__.py           # Package initialization
├── test_app.py          # App class tests
├── test_config.py       # Configuration tests
├── test_constants.py    # Constants tests
├── test_abstract.py     # Abstract repository tests
├── test_factory.py      # Factory pattern tests
├── test_grpc.py         # gRPC repository tests
├── test_postgres.py     # PostgreSQL repository tests
└── test_main.py         # Main entry point tests
```

## Mocking Strategy

- **Configuration**: Uses unittest.mock for config objects
- **Database**: Mocks psycopg2 connections and cursors
- **gRPC**: Mocks channels and service stubs
- **File I/O**: Uses mock_open for file operations

## Notes

- All tests are isolated and don't require external services
- Database and gRPC calls are fully mocked
- Tests use fixtures for reusable test data
- Parametrized tests cover multiple scenarios
- Error handling is thoroughly tested
