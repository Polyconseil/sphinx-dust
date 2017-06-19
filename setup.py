#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


def read(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='sphinx-dust',
    version='1.2.2',
    author="Polyconseil",
    author_email="opensource+sphinx-dust@polyconseil.fr",
    description="Sphinx extension to produce warnings when a doc needs proofreading.",
    license='BSD',
    keywords='sphinx documentation review proofread up-to-date',
    url='https://github.com/Polyconseil/sphinx-dust',
    packages=find_packages(exclude=['tests*']),
    long_description=read('README.rst'),
    install_requires=[
        'Sphinx>=1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    include_package_data=True,
)
