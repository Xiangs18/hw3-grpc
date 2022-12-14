# hw3-grpc

Please run the following command in service folder to generate the gRPC client and server interfaces from our .proto service definition. 

```
python -m grpc_tools.protoc -I ../protos --python_out=. --grpc_python_out=. ../protos/bookstore.proto
```
