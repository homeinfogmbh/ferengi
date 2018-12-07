"""Configuration parsing."""

from ferengi.config import ferengi_config


__all__ = ['CONFIG']


CONFIG = ferengi_config('openweathermap.conf')
