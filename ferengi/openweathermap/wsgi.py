"""WGSI application to retrieve weather data."""

from flask import request

from timelib import today
from wsgilib import JSON, XML

from ferengi.openweathermap.functions import forecasts_to_dom
from ferengi.openweathermap.orm import City, Forecast


__all__ = ['ROUTES']


def get_weather(city):
    """Returns the respective weather forecasts."""

    try:
        forecasts = Forecast.by_city(city, since=today())
    except City.DoesNotExist:
        return ('No such city.', 404)

    if 'xml' in request.args:
        return XML(forecasts_to_dom(city, forecasts))

    return JSON([forecast.to_dict() for forecast in forecasts])


ROUTES = (('GET', '/weather/<city>', get_weather, 'get_weather'),)
