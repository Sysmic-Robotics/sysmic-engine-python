# Compile protobuf files
rm -f protobuf/*.js
protoc -I=protobuf/ --js_out=import_style=commonjs,binary:protobuf/ protobuf/*.proto

# Install dependencies
npm install
