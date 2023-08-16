"""WSGI services."""

from wsgilib import Application

from ferengi import openligadb, openweathermap


__all__ = ["APPLICATION"]


APPLICATION = Application("ferengi", cors=True)
APPLICATION.add_routes(openligadb.ROUTES)
APPLICATION.add_routes(openweathermap.ROUTES)
