
find_package(Protobuf REQUIRED)
set(PROTO_FILE "${CMAKE_CURRENT_SOURCE_DIR}/proto/algo_commander.proto")
message(STATUS "cmake dir iss ${Protobuf_LIBRARIES}")
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTO_FILE})
include_directories(${CMAKE_CURRENT_BINARY_DIR})


add_executable(algo_commander
  main.cpp
  ${PROTO_SRCS} 
  ${PROTO_HDRS}
)


target_link_libraries(algo_commander
  PRIVATE
    ${Protobuf_LIBRARIES}
)

# Yep, that's it!
target_link_libraries(algo_commander
  PUBLIC
    ImGui-SFML::ImGui-SFML
    sfml-network
)


include(Install.cmake)