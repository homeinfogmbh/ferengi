"""News from RSS feed from google.com for Hannover."""

from ferengi.googlenews.client import update
from ferengi.googlenews.constants import FEEDS
from ferengi.googlenews.orm import News


__all__ = ['FEEDS', 'News', 'update']
