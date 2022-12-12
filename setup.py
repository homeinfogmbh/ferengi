#! /usr/bin/env python3
"""Installation script."""

from setuptools import setup

setup(
    name='ferengi',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'b64lzma',
        'feedparser',
        'filedb',
        'flask',
        'hwdb',
        'lxml',
        'peewee',
        'peeweeplus',
        'requests',
        'wsgilib'
    ],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info at homeinfo dot de>',
    maintainer='Richard Neumann',
    maintainer_email='<r dot neumann at homeinfo priod de>',
    packages=[
        'ferengi',
        'ferengi.openligadb',
        'ferengi.openweathermap',
        'ferengi.rssapp',
        'ferengi.spiegelnews',
        'ferengi.weltnews'
    ],
    entry_points={
        'console_scripts': [
            'ferengi = ferengi.cli:main'
        ]
    },
    data_files=[
        ('/usr/lib/systemd/system/', [
            'files/ferengi@.service',
            'files/ferengi@.timer'
        ])
    ],
    license='GPLv3',
    description=(
        'Frankly Everything, but Real Estates'
        ' Notoriously Greedy Importer.'
    )
)
