Requieres:
- Protobuf


OS: Windows 11
Problem:
''' Cmake could not load cache '''
Solution:

First configure the project:
``` cmake . ```


´´´ 
cmake -B build -G Ninja
cmake --build . ´´´

Error: Could NOT find Protobuf (missing: Protobuf_LIBRARIES Protobuf_INCLUDE_DIR)

