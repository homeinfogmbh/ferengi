"""Data import from openligadb.de."""

from datetime import date

from requests import get

from ferengi.openligadb.config import CONFIG, LOGGER
from ferengi.openligadb.dom import CreateFromDocument, Match


__all__ = ['get_table']


HEADERS = {'Accept': 'application/xml'}


def get_table(year: int = None, *, headers: dict = HEADERS) -> Match:
    """Gets the table information for the given year or the current year."""

    if year is None:
        year = date.today().year

    template = CONFIG['api']['table_url']
    url = template.format(year)
    LOGGER.info('Retrieving data from: %s', url)
    response = get(url, headers=headers)
    return CreateFromDocument(response.text)
