"""FERENGI's API."""

from subprocess import PIPE, Popen

from requests import Response

from ferengi.roa import ROA


__all__ = ['UpToDate', 'APIError', 'roa']


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


def roa():
    """Prints the rules of acquisition."""

    with Popen(('/usr/bin/less',), stdin=PIPE) as process:
        process.communicate(input=bytes(ROA))
