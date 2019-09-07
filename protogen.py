import os

PROTO_FILES_PATH = "../bolproto"
mkdirCmd = f'mkdir -p {PROTO_FILES_PATH}/bolpy/proto'
os.system(mkdirCmd)

copyBolProtoCmd = f'cp {PROTO_FILES_PATH}/bol.proto {PROTO_FILES_PATH}/bolpy/proto'
os.system(copyBolProtoCmd)

protogenCmd = 'python -m grpc_tools.protoc -I=../bolproto --python_out=. --grpc_python_out=. ../bolproto/bolpy/proto/bol.proto'
os.system(protogenCmd)
