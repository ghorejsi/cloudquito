from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cloudquito',
    version='0.0.1.dev0',
    packages=find_packages(),
    url='',
    license='gpl',
    author='Greg Horejsi',
    author_email='g.horejsi81@gmail.com',
    description='Cloud abstraction wrappers and utility functions.',
    long_description=long_description,
    install_requires=[
        'boto3'
    ],
)
