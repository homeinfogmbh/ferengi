"""Interface functions."""

from logging import getLogger

from terminallib import Deployment

from ferengi.api import APIError, UpToDate
from ferengi.openweathermap.orm import City


__all__ = ['cities', 'update']


COUNTRIES = {'DE', 'AT'}
LOGGER = getLogger('OpenWeatherMap')


def cities():
    """Yields used city names."""

    names = set()

    for deployment in Deployment:
        names.add(deployment.address.city)

    for name in names:
        try:
            yield City.get((City.name == name) & (City.country << COUNTRIES))
        except City.DoesNotExist:
            LOGGER.warning('No such city: "%s".', name)


def update(force=False):
    """Updates all weather."""

    for city in cities():
        try:
            city.update_forecast(force=force)
        except UpToDate:
            LOGGER.info('Weather for "%s" is up-to-date.', city.name)
        except APIError as api_error:
            LOGGER.error('Caught API error (%i): %s.', api_error, api_error)
        else:
            LOGGER.info('Updated weather for "%s".', city.name)
