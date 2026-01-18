PYTHON = python3
GEN_FOLDER = gen/pb
PROTO_FOLDER = proto/music

APP_SOURCE = src/main.py
TEST_SOURCE = tests/

.PHONY: all run install test clean

all: run

run:
	$(PYTHON) $(APP_SOURCE)

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest $(TEST_SOURCE)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf ${GEN_FOLDER}

gen: clean
	mkdir -p ${GEN_FOLDER}
	$(PYTHON) -m grpc_tools.protoc --proto_path=${PROTO_FOLDER} --python_out=${GEN_FOLDER} --pyi_out=${GEN_FOLDER} --grpc_python_out=${GEN_FOLDER} ${PROTO_FOLDER}/models.proto ${PROTO_FOLDER}/service.proto
