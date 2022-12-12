"""News from RSS feed from rss.app from different providers."""

from ferengi.rssapp.client import update
from ferengi.rssapp.constants import FEEDS
from ferengi.rssapp.orm import News


__all__ = ['FEEDS', 'News', 'update']
