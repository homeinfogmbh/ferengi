"""News update client."""

from logging import getLogger

from ferengi.rssapp.constants import FEEDS
from ferengi.rssapp.orm import News
from ferengi.rss import update_from_url


__all__ = ['update']


def update() -> None:
    """Update news from default RSS feed."""

    for name, url in FEEDS.items():
        getLogger('Google News').info('Importing news for feed: %s', name)
        News.delete().where(News.source == url).execute()
        update_from_url(url, News, clear=False)
