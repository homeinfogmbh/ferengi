"""WSGI services."""

from traceback import format_exc

from wsgilib import Application, Error

from ferengi import facebook, openligadb, openweathermap, garbage_disposal


__all__ = ['APPLICATION']


APPLICATION = Application('ferengi', cors=True)
APPLICATION.add_routes(facebook.ROUTES)
APPLICATION.add_routes(openligadb.ROUTES)
APPLICATION.add_routes(openweathermap.ROUTES)
APPLICATION.add_routes(garbage_disposal.ROUTES)


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Error(format_exc(), status=500)
