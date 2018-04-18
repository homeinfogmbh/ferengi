"""WSGI services."""

from datetime import datetime
from json import dumps
from traceback import format_exc

from flask import Response, Flask

from terminallib import Terminal

from ferengi.garbage_disposal import Location
from ferengi.openweathermap import City, Forecast

__all__ = ['APPLICATION']

APPLICATION = Flask('ferengi')


@APPLICATION.route('/weather/<city>')
def get_weather(city):
    """Returns the respective weather forecasts."""

    try:
        city = City.get(City.name == city)
    except City.DoesNotExist:
        return ('No such city.', 404)

    forecasts = [
        forecast.to_dict() for forecast in Forecast.select().where(
            (Forecast.city == city) &
            (Forecast.dt >= datetime.now()))]
    return Response(dumps(forecasts), mimetype='application/json')


@APPLICATION.route('/garbage-disposal/<terminal>')
def get_garbage_disposal(terminal):
    """Returns garbage disposal information for the respective terminal."""

    try:
        tid, cid = terminal.split('.')
    except ValueError:
        return ('Invalig terminal ID.', 400)

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

    return Response(dumps(locations), mimetype='application/json')


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Response(format_exc(), mimetype='text/plain', status=500)
