"""Common functions."""

from datetime import datetime

from requests import get

from filedb import File


__all__ = ['add_file_from_url', 'parse_datetime']


def add_file_from_url(url: str) -> File:
    """Downloads a file from the given URL
    and adds it to the filedb returning its ID.
    """

    return File.from_bytes(get(url).content)


def parse_datetime(timestamp: str) -> datetime:
    """Parse a datetime from a timestamp.

    The XML files inhttp://homeinfo.weltoohservice.de/xml/ have broken
    locales. It used to follow the format:

        '%a, %d %b %Y %H:%M:%S %Z'

    However, recently the day is in English locale, while the month is in
    German locale. Hence, we just strip away the day and parse the
    remainder with German locale.
    """

    _, remainder = timestamp.split(', ', maxsplit=1)
    return datetime.strptime(remainder, '%d %b %Y %H:%M:%S %Z')
