#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='latest',
    author='Richard Neumann',
    packages=['ferengi', 'ferengi.mods'],
    data_files=[('/etc', ['files/etc/ferengi.conf'])],
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer'))
