# nonsequitur.py
# by aaron montoya-moraga
# april 2017
# this setup code borrows heavily from the one of pytracery by Allison Parrish
# available at
# https://github.com/aparrish/pytracery

# to distribute, on terminal do
# python setup.py sdist
# twine upload dist/nonsequitur-x.y.z.tar.gz

# from distutils.core import setup
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf_8')

# this code was taken from the setup of pytracery
with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='nonsequitur',
    version='0.0.7',
    description='non sequitur jokes generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='aarón montoya-moraga',
    author_email='montoyamoraga@gmail.com',
    url='https://github.com/montoyamoraga/nonsequiturpy',
    packages= find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pycorpora', 'tracery'],
    license='Apache License 2.0',
    keywords='nonsequitur',
    zip_safe=True,
    classifiers = [
    'Programming Language :: Python :: 3',
    'Natural Language :: English',
    'Topic :: Artistic Software',
    ],
    python_requires='>=3.0, <4'
)
