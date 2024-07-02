#!/bin/sh
protoc -I=./ --python_out=../../src/proto_compiled/grsim --pyi_out=../../src/proto_compiled/grsim *.proto