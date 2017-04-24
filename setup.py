#nonsequitur.py
#by aaron montoya-moraga
#april 2017

#to distribute, on terminal do
#python setup.py sdist

#from distutils.core import setup
from setuptools import *

setup(
    name='nonsequitur',
    version='0.0.2',
    url='https://github.com/montoyamoraga/nonsequiturpy',
    author='aaron montoya-moraga',
    description='non sequitur text generator',
    license='MIT',
    install_requires=['spacy'],
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
)
