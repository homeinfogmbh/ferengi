"""FERENGI's API."""

from subprocess import PIPE, Popen

from peeweeplus import MySQLDatabase

from ferengi.roa import ROA


__all__ = ['UpToDate', 'APIError', 'ferengi_database', 'get_database']


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

    with Popen(('/usr/bin/less',), stdin=PIPE) as process:
        process.communicate(input=bytes(ROA))
