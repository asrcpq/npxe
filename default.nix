with import <nixpkgs>{};

python3.pkgs.buildPythonApplication rec {
	pname = "npxe";
	version = "0.0.1";

	src = ./.;
	nativeBuildInputs = [ qt5.wrapQtAppsHook python3.pkgs.setuptools ];

	propagatedBuildInputs = with python3.pkgs; [ pyqtwebengine ];

	dontWrapQtApps = true;
	preFixup = ''
		wrapQtApp $out/bin/npxe
	'';
}
