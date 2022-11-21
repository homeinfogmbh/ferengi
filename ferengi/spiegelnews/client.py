"""News update client."""

from ferengi.spiegelnews.constants import RSS_FEED_URL
from ferengi.spiegelnews.orm import News

from ferengi.rss import update_from_url


__all__ = ['update']


def update() -> None:
    """Update news from default RSS feed."""

    update_from_url(RSS_FEED_URL, News)
