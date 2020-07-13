"""XSD and class bindings and ORM models for welt.de API."""

from ferengi.weltnews.orm import News
from ferengi.weltnews.client import update


__all__ = ['update', 'News']
