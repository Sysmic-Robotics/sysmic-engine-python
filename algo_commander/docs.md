cd build
cmake ..

cd proto
protoc --cpp_out=. algo_commander.proto

protoc --python_out=. algo_commander.proto

Libreria para leer packetes
sudo apt install qt6-base-dev
