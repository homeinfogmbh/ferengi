#! /usr/bin/env python3

from distutils.core import setup

setup(
    name='ferengi',
    version='latest',
    author='Richard Neumann',
    packages=['ferengi'],
    data_files=[
        ('/usr/bin/', ['files/ferengi']),
        ('/usr/lib/systemd/system/',
         ['files/ferengi@.service',
          'files/ferengi@.timer']),
        ('/usr/share/', ['files/ferengi.wsgi', 'files/roa.xz']),
        ('/etc/uwsgi/apps-available/', ['files/ferengi.ini'])],
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer'))
