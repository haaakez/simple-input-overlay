{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    (python3.withPackages (ps: with ps; [
      websockets
      evdev
    ]))
    libevdev
  ];

  shellHook = ''
    echo "Python, websockets, and evdev are ready."
  '';
}
