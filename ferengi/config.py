"""HEED's main configuration"""

from configparser import ConfigParser

__date__ = "05.02.2015"
__author__ = "Richard Neumann <r.neumann@homeinfo.de>"
__all__ = ['core', 'ipc', 'display', 'update']

CONFIG_FILE = '/usr/local/etc/heed.conf'

config = ConfigParser()
config.read(CONFIG_FILE)

core = config['core']
weather = config['weather']
facebook = config['facebook']
news = config['news']
quotes = config['quotes']
guess_picture = config['guess_picture']
