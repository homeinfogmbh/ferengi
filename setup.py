#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='latest',
    author='Richard Neumann',
    packages=['ferengi'],
    scripts=['files/ferengi', 'files/ferengid'],
    data_files=[
        ('/usr/lib/systemd/system/',
         ['files/ferengi.service',
          'files/ferengi@.service',
          'files/ferengi@.timer']),
        ('/usr/share/', ['files/roa.xz'])],
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer'))
