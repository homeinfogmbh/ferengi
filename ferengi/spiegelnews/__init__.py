"""News from RSS feed of spiegel.de."""

from ferengi.spiegelnews.client import update
from ferengi.spiegelnews.orm import News


__all__ = ['News', 'update']
