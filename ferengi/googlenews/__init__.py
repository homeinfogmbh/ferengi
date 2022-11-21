"""News from RSS feed from google.com for Hannover."""

from ferengi.googlenews.client import update
from ferengi.googlenews.orm import News


__all__ = ['News', 'update']
