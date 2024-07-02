# Start engine as a background process and save the proccess on a variable
./engine/builddir/sysmic-engine & ENGINE=$!

# Start the GUI kill engine when closed
cd ui &&
npm start
kill $ENGINE
