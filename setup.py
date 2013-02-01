import os

from setuptools import setup, find_packages

if os.path.exists('README.rst'):
    with open('README.rst') as file:
        long_description = file.read()
else:
    long_description = ''

setup(
    name="geventreactor",
    long_description=long_description,
    version="0.2",
    packages=find_packages(),

    install_requires=[
        'gevent>=1.0',
    ],

    author="Erik Allik",
    author_email="eallik@gmail.com",
    license="BSD",
    url="http://github.com/eallik/geventreactor/"
)
