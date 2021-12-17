import setuptools

setuptools.setup(
	name = "npxe",
	version = "0.0.1",
	packages = setuptools.find_packages(),
	entry_points = {
		"gui_scripts": ["npxe = npxe.__main__:main"],
	},
	python_requires = ">=3.6",
)
