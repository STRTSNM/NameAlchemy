# shell.nix

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "python3.10-environment";

  buildInputs = [
    (pkgs.python310)
    (pkgs.python310Packages.requests)
    (pkgs.python310Packages.beautifulsoup4)
    (pkgs.git)
  ];
}

