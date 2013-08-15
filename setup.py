#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'pydsignals',
    version = ":versiontools:pydsignals:",
    description = "Python generic signals abstraction library",
    long_description = "",
    keywords = 'data, signals',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/jespino/pydsignals',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    package_data={},
    install_requires=[
        'six',
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.2.1', 'mock >= 1.0.1'],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
