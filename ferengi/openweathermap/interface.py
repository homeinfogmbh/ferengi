"""Interface functions."""

from logging import getLogger
from typing import Iterator

from peewee import ModelSelect

from hwdb import Deployment

from ferengi.api import APIError, UpToDate
from ferengi.openweathermap.config import CONFIG
from ferengi.openweathermap.orm import City


__all__ = ['cities', 'update']


LOGGER = getLogger('OpenWeatherMap')


def names() -> Iterator[str]:
    """Yields targeted city names."""

    for name in CONFIG['config'].get('cities', '').split():
        yield name

    for deployment in Deployment.select(cascade=True).where(True):
        yield deployment.address.city


def cities() -> ModelSelect:
    """Yields used city names."""

    return City.select().where(
        (City.name << set(names()))
        & (City.country << set(CONFIG['config']['countries'].split()))
    )


def update(force: bool = False) -> None:
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
