with import <nixpkgs> { };

mkShell {
    buildInputs = [
        meson
        ninja
        pkg-config
        protobuf
        qt5.qtwebsockets
        armadillo
        nodejs
        nodePackages.npm
    ];
}
