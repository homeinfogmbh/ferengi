"""Data import from openligadb.de."""

from ferengi.openligadb.client import get_table
from ferengi.openligadb.config import CONFIG
from ferengi.openligadb.orm import Team
from ferengi.openligadb.wsgi import ROUTES


__all__ = ["CONFIG", "ROUTES", "get_table", "Team"]
