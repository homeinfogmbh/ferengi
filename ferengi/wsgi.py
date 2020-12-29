"""WSGI services."""

from traceback import format_exc

from wsgilib import Application, Error

from ferengi import facebook, openligadb, openweathermap, garbage_disposal


__all__ = ['APPLICATION']


APPLICATION = Application('ferengi', cors=True)
ROUTES = (
    *facebook.ROUTES, *openligadb.ROUTES, *openweathermap.ROUTES,
    *garbage_disposal.ROUTES
)
APPLICATION.add_routes(ROUTES)


@APPLICATION.errorhandler(Exception)
def debug_exceptions(_):
    """Prints a stack trace."""

    return Error(format_exc(), status=500)
