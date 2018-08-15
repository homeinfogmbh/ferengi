"""Garbage disposal module."""

from ferengi.garbage_disposal.orm import Location
from ferengi.garbage_disposal.wsgi import ROUTES

__all__ = ['ROUTES', 'Location']
