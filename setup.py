#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='latest',
    author='Richard Neumann',
    packages=['ferengi'],
    data_files=[('/etc/ferengi.d', ['files/etc/ferengi.d/weather.conf'])],
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer'))
