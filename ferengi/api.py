"""FERENGI's API."""

from configparser import ConfigParser
from subprocess import PIPE, Popen

from flask import Response

from peeweeplus import MySQLDatabase

from ferengi.roa import ROA


__all__ = ['UpToDate', 'APIError', 'get_database']


class UpToDate(Exception):
    """Indicates that the record is up to date."""


class APIError(Exception):
    """Indicates that data could not be received from the API."""

    def __init__(self, response: Response):
        """Sets status code and response text."""
        super().__init__(response.text)
        self.response = response

    def __int__(self):
        """Returns the status code."""
        return self.response.status_code

    def __str__(self):
        """Returns the response text."""
        return self.response.text


class FerengiDatabase(MySQLDatabase):
    """FERENGI database."""

    @property
    def database(self) -> str:
        """Returns the database name with a prefix."""
        return f'ferengi_{super().database}'

    @database.setter
    def database(self, database: str) -> None:
        """Sets the databast name."""
        super().database = database

    @property
    def host(self) -> str:
        """Returns the host name."""
        return super().host or 'localhost'

    @host.setter
    def host(self, host: str) -> None:
        """Sets the host name."""
        super().host = host


def get_database(config: ConfigParser) -> MySQLDatabase:
    """Returns the database by config."""

    return FerengiDatabase(config=config['db'])


def roa():
    """Prints the rules of acquisition."""

    with Popen(('/usr/bin/less',), stdin=PIPE) as process:
        process.communicate(input=bytes(ROA))
