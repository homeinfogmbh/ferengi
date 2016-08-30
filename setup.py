#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='0.1-indev',
    author='Richard Neumann',
    author_email='r.neumann@homeinfo.de',
    packages=['ferengi', 'ferengi.mods'],
    data_files=[('/etc', ['files/etc/ferengi.conf'])],
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer'))
