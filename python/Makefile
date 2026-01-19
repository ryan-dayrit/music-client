PYTHON = python3
GEN_FOLDER = .
PROTO_FOLDER = ../proto
MODULE = music.client

.PHONY: all run clean

all: run

run_db_fetch: gen
	$(PYTHON) -m $(MODULE) --source=database

run_svc_fetch: gen
	$(PYTHON) -m $(MODULE) --source=service

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*_pb2.py" -delete
	find . -type f -name "*_pb2.pyi" -delete
	find . -type f -name "*_pb2_grpc.py" -delete

gen: clean
	mkdir -p ${GEN_FOLDER}
	$(PYTHON) -m grpc_tools.protoc --proto_path=${PROTO_FOLDER} --python_out=${GEN_FOLDER} --pyi_out=${GEN_FOLDER} --grpc_python_out=${GEN_FOLDER} ${PROTO_FOLDER}/service.proto ${PROTO_FOLDER}/models.proto
