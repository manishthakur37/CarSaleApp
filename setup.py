from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in carsale/__init__.py
from carsale import __version__ as version

setup(
	name="carsale",
	version=version,
	description=" your car sale",
	author="manish kumar",
	author_email="mk885770@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
