"""Interface functions."""

from logging import getLogger

from terminallib import Deployment

from ferengi.api import APIError, UpToDate
from ferengi.openweathermap.aliases import load_aliases
from ferengi.openweathermap.orm import City


LOGGER = getLogger('OpenWeatherMap')


__all__ = ['update']


def used_cities():
    """Yields used city names."""

    cities = set()

    for deployment in Deployment:
        cities.add(deployment.address.city)

    aliases = load_aliases()
    return {aliases.get(city, city) for city in cities}


def update(force=False):
    """Updates all weather."""

    for city in used_cities():
        try:
            city = City.get(City.name == city)
        except City.DoesNotExist:
            LOGGER.warning('No such city: %s', city)
            continue

        try:
            city.update_forecast(force=force)
        except UpToDate:
            LOGGER.info('Weather for "%s" is up-to-date.', city.name)
        except APIError as api_error:
            LOGGER.error('Caught API error (%i): %s.', api_error, api_error)
        else:
            LOGGER.info('Updated weather for "%s".', city.name)
