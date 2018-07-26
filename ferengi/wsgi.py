"""WSGI services."""

from datetime import datetime
from traceback import format_exc

from flask import request

from terminallib import Terminal
from wsgilib import Application, Error, JSON, XML

from ferengi.garbage_disposal import Location
from ferengi.openweathermap import forecasts_to_dom, City, Forecast


__all__ = ['APPLICATION']


APPLICATION = Application('ferengi', cors=True)


@APPLICATION.route('/weather/<city>')
def get_weather(city):
    """Returns the respective weather forecasts."""

    try:
        city = City.get(City.name == city)
    except City.DoesNotExist:
        return ('No such city.', 404)

    forecasts = Forecast.select().where(
        (Forecast.city == city) &
        (Forecast.dt >= datetime.now()))

    if 'xml' in request.args:
        return XML(forecasts_to_dom(city, forecasts))

    return JSON([forecast.to_dict() for forecast in forecasts])


@APPLICATION.route('/garbage-disposal/<terminal>')
def get_garbage_disposal(terminal):
    """Returns garbage disposal information for the respective terminal."""

    try:
        tid, cid = terminal.split('.')
    except ValueError:
        return ('Invalid terminal ID.', 400)

    try:
        terminal = Terminal.by_ids(cid, tid)
    except Terminal.DoesNotExist:
        return ('No such terminal.', 404)

    try:
        address = terminal.location.address
    except AttributeError:
        return ('Terminal is not located.', 400)

    locations = [
        location.to_dict() for location in Location.by_address(address)]

    if not locations:
        return ('No garbage disposal information available.', 404)

    return JSON(locations)


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Error(format_exc(), status=500)
