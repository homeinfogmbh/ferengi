"""Configuration parsing."""

from configlib import INIParser


__all__ = ['CONFIG']


CONFIG = INIParser('/etc/ferengi.d/openweathermap.conf')
