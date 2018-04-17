"""WSGI services."""

from datetime import datetime
from json import dumps
from traceback import format_exc

from flask import jsonify, Response, Flask

from terminallib import Terminal

from ferengi.garbage_disposal import GarbageDisposal
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

    try:
        result = GarbageDisposal.by_address(address)
    except GarbageDisposal.DoesNotExist:
        return ('No garbage disposal information available.', 404)

    return Response(dumps(result), mimetype='application/json')


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Response(format_exc(), mimetype='text/plain', status=500)
