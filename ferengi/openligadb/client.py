"""Data import from openligadb.de."""

from datetime import date
from typing import Optional

from requests import get

from ferengi.openligadb.config import CONFIG, LOGGER


__all__ = ["get_table"]


def get_table(year: Optional[int] = None) -> list[dict]:
    """Gets the table information for the given year or the current year."""

    if year is None:
        year = date.today().year

    template = CONFIG["api"]["table_url"]
    url = template.format(year)
    LOGGER.info("Retrieving data from: %s", url)
    return get(url).json()
