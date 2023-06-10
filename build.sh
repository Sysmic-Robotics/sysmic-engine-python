# Compile engine and protobuf files
cd engine
./build.sh

# Return to root folder
cd ..

# Install dependencies and compile protobuf files
cd ui
./build.sh
