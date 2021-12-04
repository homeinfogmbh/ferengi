"""Garbage disposal module configuration."""

from datetime import timedelta
from logging import getLogger

from ferengi.config import ferengi_config


__all__ = ['CONFIG', 'INTERVAL', 'DISTRICTS', 'WAIT_TIME']


LOGGER = getLogger('Garbage disposal')
CONFIG = ferengi_config('garbage_disposal.conf')

try:
    INTERVAL = CONFIG.getint('api', 'interval')
except KeyError:
    INTERVAL = 24
    LOGGER.warning('Interval unconfigured. Defaulting to %ih.', INTERVAL)

INTERVAL = timedelta(hours=INTERVAL)

try:
    DISTRICTS = CONFIG.get('api', 'districts')
except KeyError:
    DISTRICTS = ['Hannover']
    LOGGER.warning('Districts unconfigured. Defaulting to %s.', DISTRICTS)
else:
    DISTRICTS = DISTRICTS.split()

try:
    WAIT_TIME = CONFIG.getint('api', 'wait_time')
except KeyError:
    WAIT_TIME = 30
    LOGGER.warning('Wait time unconfigured. Defaulting to %is.', WAIT_TIME)
