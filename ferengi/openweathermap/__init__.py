"""OpenWeatherMap API."""

from ferengi.openweathermap.functions import forecasts_to_dom
from ferengi.openweathermap.interface import update
from ferengi.openweathermap.orm import City, Forecast
from ferengi.openweathermap.wsgi import ROUTES


__all__ = [
    'ROUTES',
    'forecasts_to_dom',
    'openweathermap',
    'update',
    'City',
    'Forecast']


openweathermap = update     # pylint: disable=C0103
