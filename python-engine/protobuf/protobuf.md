### Protobuf

Esta carpeta consiste en las definiciones provistas por SSL Robocup de estructuras para la mensajería de datos serializados por medio de protobuf.

La compilación manual se realiza dentro del directorio `protobuf`

```protoc -I=robocup_ssl --python_out=../src/proto_compiled --pyi_out=../src/proto_compiled robocup_ssl/*.proto```

Para la eliminación manual de este directorio puede usar

```rm -f ../src/proto_compiled/*.py ../src/proto_compiled/__pycache__/*.pyc```

La compilación del archivo de ui se hace en

```protoc -I=. --python_out=../src/proto_compiled --pyi_out=../src/proto_compiled /*.proto```