with import <nixpkgs> {};

let myPythonPackages = python3.withPackages (p: with p; [
	numpy
]);

in pkgs.mkShell {
  buildInputs = with pkgs; [
	myPythonPackages
	jupyter
  ];
}
