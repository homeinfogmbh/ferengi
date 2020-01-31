"""RSS feed configuration."""

from logging import getLogger

from ferengi.api import get_database
from ferengi.config import ferengi_config


__all__ = ['CONFIG', 'DATABASE']


LOGGER = getLogger('openligadb')
CONFIG = ferengi_config('rssfeed.conf')
DATABASE = get_database(CONFIG)
