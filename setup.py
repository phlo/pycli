from setuptools import setup

import pycli

setup(
    name = pycli.__name__,
    version = pycli.__version__,
    license = pycli.__license__,
    description = pycli.__doc__,
    author = pycli.__author__,
    author_email = pycli.__email__,
    url = pycli.__url__,
    packages = [pycli.__name__]
)
