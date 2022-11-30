"""News update client."""

from logging import getLogger

from ferengi.googlenews.constants import CITIES
from ferengi.googlenews.orm import News
from ferengi.rss import update_from_url


__all__ = ['update']


def update() -> None:
    """Update news from default RSS feed."""

    for city, url in CITIES.items():
        getLogger('Google News').info('Importing news for city: %s', city)
        News.delete().where(News.source == url).execute()
        update_from_url(url, News, clear=False, city=city)
