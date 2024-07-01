cd build
cmake ..

cd proto
protoc --cpp_out=. algo_commander.proto

protoc --python_out=. algo_commander.proto


CMake >= 3.12

Also, if you're on Linux, you'll need to install dependencies for building SFML
specified
[here](https://www.sfml-dev.org/tutorials/2.5/compile-with-cmake.php#installing-dependencies).