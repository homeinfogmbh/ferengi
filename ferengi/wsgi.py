"""WSGI services"""

from datetime import datetime

from peewee import DoesNotExist
from wsgilib import Error, JSON, ResourceHandler

from ferengi.weather import City, Forecast

__all__ = ['SERVICES']


class WeatherHandler(ResourceHandler):
    """Handles weather queries"""

    def get(self):
        """Handles GET requests"""
        if self.resource is not None:
            raise Error('No city specified.') from None
        else:
            try:
                city = City.get(City.name == self.resource)
            except DoesNotExist:
                raise Error('No such city.', status=404) from None
            else:
                forecasts = [
                    forecast.to_dict() for forecast in Forecast.select().where(
                        (Forecast.city == city) &
                        (Forecast.timestamp >= datetime.now()))]
                return JSON(forecasts)


SERVICES = {
    'weather': WeatherHandler}
