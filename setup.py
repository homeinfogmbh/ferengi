#! /usr/bin/env python3

from distutils.core import setup

setup(
	name='PyExposeAgent',
	version='0.1-indev',
	author='Richard Neumann',
	author_email='mail@richard-neumann.de',
	package_dir = {'homie': ''},
	packages=['homie.interfaces.exposeagent',
			'homie.translators.exposeagent'],
	data_files=[],
	license=open('LICENSE.txt').read(),
	description='Interface implementation for the Exposé-Agent client program of the HOMEINFO GmbH',
	long_description=open('README.txt').read(),
)
