import os

PROTO_FILES_PATH = "../proto_files"
mkdirCmd = f'mkdir -p {PROTO_FILES_PATH}/bolpy/proto'
os.system(mkdirCmd)

copyBolProtoCmd = f'cp {PROTO_FILES_PATH}/bol.proto {PROTO_FILES_PATH}/bolpy/proto'
os.system(copyBolProtoCmd)

protogenCmd = 'python -m grpc_tools.protoc -I=../proto_files --python_out=. --grpc_python_out=. ../proto_files/bolpy/proto/bol.proto'
os.system(protogenCmd)
