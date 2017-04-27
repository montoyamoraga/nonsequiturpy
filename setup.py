#nonsequitur.py
#by aaron montoya-moraga
#april 2017
#this setup code borrows heavily from the one of pytracery by Allison Parrish
#available at
#https://github.com/aparrish/pytracery

#to distribute, on terminal do
#python setup.py sdist
#twine upload dist/nonsequitur-x.y.z.tar.gz

#from distutils.core import setup
from setuptools import *

#this code was taken from the setup of pytracery
with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='nonsequitur',
    version='0.0.5',
    description='non sequitur text generator, mainly jokes',
    long_description= readme,
    author='aaron montoya-moraga',
    author_email='aammontoya@gmail.com',
    url='https://github.com/montoyamoraga/nonsequiturpy',
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pycorpora', 'tracery'],
    license='Apache License 2.0',
    keywords='nonsequitur',
    zip_safe=True,
    classifiers = [
    'Programming Language :: Python :: 2.7',
    'Natural Language :: English',
    'Topic :: Artistic Software',
    ]
)
