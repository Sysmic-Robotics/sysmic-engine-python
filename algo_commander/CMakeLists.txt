cmake_minimum_required(VERSION 3.0)
project(sfml_interface)

# Find SFML package
find_package(SFML 2.5 COMPONENTS graphics network REQUIRED)

# Find Protobuf package
find_package(Protobuf REQUIRED)

# Set path to your .proto file
set(PROTO_FILE "${CMAKE_CURRENT_SOURCE_DIR}/src/proto/algo_commander.proto")

# Generate C++ code from your .proto file
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTO_FILE})

# Include generated files in the project
include_directories(${CMAKE_CURRENT_BINARY_DIR})

# Add your executable and link against Protobuf
add_executable(sfml_interface main.cpp ${PROTO_SRCS} ${PROTO_HDRS})


# Link SFML libraries
target_link_libraries(sfml_interface PRIVATE sfml-graphics sfml-network ${Protobuf_LIBRARIES})
