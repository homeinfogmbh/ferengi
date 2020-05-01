"""Common functions."""

from requests import get

from filedb import File


__all__ = ['add_file_from_url']


def add_file_from_url(url):
    """Downloads a file from the given URL
    and adds it to the filedb returning its ID.
    """

    return File.from_bytes(get(url).content)
