from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.7'
DESCRIPTION = 'MCDM implementation using Topsis for numerical data'

# Setting up
setup(
    name="GopaleshTopsis",
    version=VERSION,
    author="Gopalesh Bansal",
    author_email="<gopalesh2002@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['scipy', 'numpy', 'pandas'],
    keywords=['python', 'topsis', 'weights', 'impacts'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)