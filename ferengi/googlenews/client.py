"""News update client."""

from ferengi.googlenews.constants import CITIES
from ferengi.googlenews.orm import News
from ferengi.rss import update_from_url


__all__ = ['update']


def update() -> None:
    """Update news from default RSS feed."""

    for city, url in CITIES.items():
        update_from_url(url, News, city=city)
