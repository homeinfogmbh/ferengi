"""Ferengi main configuiration."""

from configlib import INIParser

__all__ = ['CONFIG']


CONFIG = INIParser('/etc/ferengi.conf')
