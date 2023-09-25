from distutils.core import setup
import os
from setuptools import find_packages

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""
    
# Defines __version__
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, "pybop", "version.py")) as f:
    exec(f.read())

setup(
    name="pybop",
    packages=find_packages("."),
    version=__version__,
    license="BSD-3-Clause",
    description="Python Battery Optimisation and Parameterisation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pybop-team/PyBOP",
    install_requires=[
        "pybamm>=23.1",
        "numpy>=1.16",
        "scipy>=1.3",
        "pandas>=1.0",
        "nlopt>=2.6",
    ],
    # https://pypi.org/classifiers/
    classifiers=[],
    python_requires=">=3.8,<=3.12",
)
