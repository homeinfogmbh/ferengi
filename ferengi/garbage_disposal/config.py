"""Garbage disposal module configuration."""

from datetime import timedelta
from logging import getLogger

from configlib import INIParser

from ferengi.api import get_database


__all__ = ['CONFIG', 'DATABASE', 'INTERVAL', 'DISTRICTS', 'WAIT_TIME']


LOGGER = getLogger('Garbage disposal')
CONFIG = INIParser('/etc/ferengi.d/garbage_disposal.conf')
DATABASE = get_database(CONFIG)

try:
    INTERVAL = CONFIG['api']['interval']
except KeyError:
    INTERVAL = 24
    LOGGER.warning('Interval unconfigured. Defaulting to %ih.', INTERVAL)
else:
    INTERVAL = int(INTERVAL)

INTERVAL = timedelta(hours=INTERVAL)

try:
    DISTRICTS = CONFIG['api']['districts']
except KeyError:
    DISTRICTS = ['Hannover']
    LOGGER.warning('Districts unconfigured. Defaulting to %s.', DISTRICTS)
else:
    DISTRICTS = DISTRICTS.split()

try:
    WAIT_TIME = CONFIG['api']['wait_time']
except KeyError:
    WAIT_TIME = 30
    LOGGER.warning('Wait time unconfigured. Defaulting to %is.', WAIT_TIME)
else:
    WAIT_TIME = int(WAIT_TIME)
