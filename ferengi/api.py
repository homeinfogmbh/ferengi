"""FERENGI's API."""

from io import BytesIO
from subprocess import Popen

from peeweeplus import MySQLDatabase
from syslib import B64LZMA


__all__ = ['UpToDate', 'APIError', 'ferengi_database', 'get_database']


ROA = B64LZMA(
    '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')


class UpToDate(Exception):
    """Indicates that the record is up to date."""


class APIError(Exception):
    """Indicates that data could not be received from the API."""

    def __init__(self, response):
        """Sets status code and response text."""
        super().__init__(response.text)
        self.response = response

    def __int__(self):
        """Returns the status code."""
        return self.response.status_code

    def __str__(self):
        """Returns the response text."""
        return self.response.text


def ferengi_database(database, user=None, passwd=None):
    """Returns a local, prefixed MySQL database."""

    return MySQLDatabase(
        'ferengi_{}'.format(database), host='localhost', user=user,
        passwd=passwd, closing=True)


def get_database(config):
    """Returns the database by config."""

    return ferengi_database(
        config['db']['database'], user=config['db']['user'],
        passwd=config['db']['passwd'])


def roa():
    """Prints the rules of acquisition."""

    stdin = BytesIO(ROA.__bytes__())
    return Popen(('/usr/bin/less',), stdin=stdin)
