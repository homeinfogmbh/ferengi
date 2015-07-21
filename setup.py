#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='0.1-indev',
    author='Richard Neumann',
    author_email='r.neumann@homeinfo.de',
    install_requires=['homie'],
    packages=['ferengi'],
    data_files=[('/etc', ['files/etc/ferengi.conf'])],
    license=open('LICENSE.txt').read(),
    description=('Frankly Everything, but Real Estates'
                 ' Notoriously Greedy Importer'),
    long_description=open('README.txt').read(),
    )
