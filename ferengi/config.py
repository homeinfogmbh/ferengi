"""FERENGI's main configuration"""

from configparser import ConfigParser

__date__ = "05.02.2015"
__author__ = "Richard Neumann <r.neumann@homeinfo.de>"
__all__ = ['core', 'db', 'facebook', 'guess_pic', 'news', 'quotes', 'weather']

CONFIG_FILE = '/usr/local/etc/ferengi.conf'

config = ConfigParser()
config.read(CONFIG_FILE)

core = config['core']
db = config['db']
facebook = config['facebook']
guess_pic = config['guess_pic']
news = config['news']
quotes = config['quotes']
weather = config['weather']
