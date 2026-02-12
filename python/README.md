# Python Music Client

## Running Tests

### Installation
```bash
pip install -r requirements-test.txt
```

### Test Commands
```bash
make test                    # Run all tests
make test-verbose            # Run with verbose output
make test-vv                 # Run with very verbose output
make test-coverage           # Run with coverage report
make test-coverage-html      # Generate HTML coverage report
```

### Direct pytest Commands
```bash
pytest                                    # Run all tests
pytest -v                                 # Verbose output
pytest tests/test_app.py                  # Run specific file
pytest tests/test_config.py::TestConfig   # Run specific class
pytest --cov=music --cov-report=html      # HTML coverage
```

## Test Coverage

The test suite includes **8 test files** with comprehensive coverage:

- **test_app.py** - App class and application logic (8 tests)
- **test_config.py** - Configuration classes (30+ tests)
- **test_constants.py** - Constants validation (7 tests)
- **test_abstract.py** - Abstract repository interface (7 tests)
- **test_factory.py** - Repository factory pattern (13 tests)
- **test_grpc.py** - gRPC repository (9 tests)
- **test_postgres.py** - PostgreSQL repository (12 tests)
- **test_main.py** - Main entry point (5 tests)

All tests use mocking for external dependencies (database, gRPC) and run without requiring external services.

## Go vs Python 
  * https://www.techtarget.com/searchitoperations/tip/Compare-Go-vs-Python-What-are-the-differences
  * https://medium.com/@vectorvarma0303/go-vs-python-a-beginners-honest-comparison-7b9b6eac1647

# Project Structure 
  * https://docs.python-guide.org/writing/structure/
  * https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6

# __main__.py
  * https://medium.com/@jameskabbes/adding-main-py-to-your-python-package-ff0cba4b8f98
  * https://stackoverflow.com/questions/4042905/what-is-main-py

# config 
  * https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/
  
# Protobuf and gRPC
  * https://www.pantsbuild.org/dev/docs/python/integrations/protobuf-and-grpc
  * https://grpc.io/docs/languages/python/basics/
  * https://medium.com/@coderviewer/simple-usage-of-grpc-with-python-f714d9f69daa

# REST vs gRPC 
  * https://blog.logrocket.com/grpc-vs-rest/#:~:text=Both%20API%20patterns%20have%20their,Happy%20API%20building!
