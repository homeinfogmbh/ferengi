"""WSGI services."""

from traceback import format_exc

from wsgilib import Application, Error

from ferengi import openweathermap, garbage_disposal


__all__ = ['APPLICATION']


APPLICATION = Application('ferengi', cors=True)
APPLICATION.add_routes(openweathermap.ROUTES, garbage_disposal.ROUTES)


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Error(format_exc(), status=500)
