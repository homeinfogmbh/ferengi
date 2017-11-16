"""WSGI services."""

from datetime import datetime

from peewee import DoesNotExist
from wsgilib import Error, JSON, RestHandler, Router

from ferengi.openweathermap import City, Forecast

__all__ = ['ROUTER']


ROUTER = Router()


@ROUTER.route('/weather/<city>')
class WeatherHandler(RestHandler):
    """Handles weather queries."""

    def get(self):
        """Handles GET requests."""
        try:
            city = City.get(City.name == self.vars['city'])
        except DoesNotExist:
            raise Error('No such city.', status=404) from None
        else:
            forecasts = [
                forecast.to_dict() for forecast in Forecast.select().where(
                    (Forecast.city == city) &
                    (Forecast.dt >= datetime.now()))]
            return JSON(forecasts)
