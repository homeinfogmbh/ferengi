"""Data import from openligadb.de."""

from datetime import date

from requests import get

from ferengi.openligadb.config import CONFIG
from ferengi.openligadb.dom import CreateFromDocument   # pylint: disable=E0611


__all__ = ['get_table']


HEADERS = {'Accept': 'application/xml'}


def get_table(year=None, *, headers=HEADERS):
    """Gets the table information for the given year or the current year."""

    if year is None:
        year = date.today().year

    template = CONFIG['api']['table_url']
    url = template.format(year)
    response = get(url, headers=headers)
    return CreateFromDocument(response.text)
