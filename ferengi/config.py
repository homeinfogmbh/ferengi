"""Ferengi config path."""

from configparser import ConfigParser
from pathlib import Path


__all__ = ['ferengi_config']


CONFIG_DIR = Path('/usr/local/etc/ferengi.d')


def ferengi_config(filename):
    """Returns a configuration for the respective file name."""

    path = CONFIG_DIR.joinpath(filename)
    config = ConfigParser()
    config.read(str(path))
    return config
