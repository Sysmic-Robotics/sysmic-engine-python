# Sysmic Engine

## Building

First to create the build environment:
```
nix-shell
```

Then:

```
./build.sh
```

## Running the project
```
./run.sh
```

There is also a README in each project with the instructions to build them and run them separatly.


## using python engine
```
cd python-engine
python3 -m venv engine-env
source engine-env/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

## Install GUI
```
cd algo_commander
mkdir build
cd build
sudo apt-get install libfreetype6-dev 
cmake ..
```

### Compile and using the GUI
```
make
src/algo_commander
```

