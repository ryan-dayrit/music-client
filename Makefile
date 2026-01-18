PYTHON = python3
GEN_FOLDER = gen/pb
PROTO_FOLDER = proto
MODULE = music.client

.PHONY: all run install clean

all: run

run: gen
	$(PYTHON) -m $(MODULE)

install:
	$(PYTHON) -m pip install -r requirements.txt

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf gen

gen: clean
	mkdir -p ${GEN_FOLDER}
	$(PYTHON) -m grpc_tools.protoc --proto_path=${PROTO_FOLDER} --python_out=${GEN_FOLDER} --pyi_out=${GEN_FOLDER} --grpc_python_out=${GEN_FOLDER} ${PROTO_FOLDER}/models.proto ${PROTO_FOLDER}/service.proto
