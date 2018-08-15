"""Facebook configuration."""

from configlib import INIParser


__all__ = ['CONFIG']


CONFIG = INIParser('/etc/ferengi.d/facebook.conf')
