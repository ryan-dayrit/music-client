PYTHON = python3
GEN_FOLDER = .
PROTO_FOLDER = ../proto
MODULE = music.client

.PHONY: all run clean test

all: run

run_db_fetch: gen
	$(PYTHON) -m $(MODULE) --source=database

run_svc_fetch: gen
	$(PYTHON) -m $(MODULE) --source=service

test:
	$(PYTHON) -m pytest

test-verbose:
	$(PYTHON) -m pytest -v

test-vv:
	$(PYTHON) -m pytest -vv

test-coverage:
	$(PYTHON) -m pytest --cov=music --cov-report=term-missing

test-coverage-html:
	$(PYTHON) -m pytest --cov=music --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*_pb2.py" -delete
	find . -type f -name "*_pb2.pyi" -delete
	find . -type f -name "*_pb2_grpc.py" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

gen: clean
	mkdir -p ${GEN_FOLDER}
	$(PYTHON) -m grpc_tools.protoc --proto_path=${PROTO_FOLDER} --python_out=${GEN_FOLDER} --pyi_out=${GEN_FOLDER} --grpc_python_out=${GEN_FOLDER} ${PROTO_FOLDER}/service.proto ${PROTO_FOLDER}/models.proto
