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

    content_type = request.headers.get('Accept', 'application/json')

    if content_type == 'application/xml':
        return XML(forecasts_to_dom(city, forecasts))

    if content_type == 'application/json':
        return JSON([forecast.to_json() for forecast in forecasts])

    return ('Invalid content type.', 406)


ROUTES = (('GET', '/weather/<city>', get_weather, 'get_weather'),)
