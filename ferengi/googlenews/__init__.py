"""News from RSS feed from google.com for Hannover."""

from ferengi.spiegelnews.client import update
from ferengi.spiegelnews.orm import News


__all__ = ['News', 'update']
