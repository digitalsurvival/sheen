#!/usr/bin/env python3

import os
from sheen.sheen import __author__,__email__,__description__,__source__,__version__,__package__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author=__author__,
    author_email=__email__,
    name=__package__,
    version=__version__,
    description=__description__,
    url=__source__,
    license='MIT',
    keywords='desktop screenshot boasting tool',
    packages=[__package__],
    install_requires=['docopt'],
    long_description=read('readme.md'),
    py_modules=[__package__],
)
