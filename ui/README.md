# Sysmic Engine GUI

To create build environment:
```
cd ..
nix-shell
cd ui
```

## To compile protobuf messages
```
protoc -I=protobuf/ --js_out=import_style=commonjs,binary:protobuf/ protobuf/*.proto
```

## To run
```
npm install
npm start
```
