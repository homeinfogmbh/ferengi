"""Openligadb module configuration."""

from logging import getLogger

from ferengi.config import ferengi_config


__all__ = ["CONFIG", "LOGGER"]


CONFIG = ferengi_config("openligadb.conf")
LOGGER = getLogger("openligadb")
