"""WSGI services."""

from traceback import format_exc

from wsgilib import Application, Error

from ferengi import openligadb, openweathermap, garbage_disposal


__all__ = ['APPLICATION']


APPLICATION = Application('ferengi', cors=True)
APPLICATION.add_routes(openligadb.ROUTES)
APPLICATION.add_routes(openweathermap.ROUTES)
APPLICATION.add_routes(garbage_disposal.ROUTES)
