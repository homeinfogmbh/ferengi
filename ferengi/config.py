"""Ferengi config path."""

from configparser import ConfigParser, SectionProxy
from pathlib import Path
from typing import Any


__all__ = ['ferengi_config']


CONFIG_DIR = Path('/usr/local/etc/ferengi.d')


class ConfigProxy(ConfigParser):
    """Configuration parser proxy."""

    def __init__(self, filename: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.loaded = False

    def __getitem__(self, item: str) -> SectionProxy:
        """Load and delegate to super method."""
        self.load()
        return super().__getitem__(item)

    @property
    def path(self) -> Path:
        """Returns the full config file path."""
        return CONFIG_DIR / self.filename

    def get(self, *args, **kwargs) -> Any:
        """Load and delegate to super method."""
        self.load()
        return super().get(*args, **kwargs)

    def load(self) -> None:
        """Loads the config file."""
        if not self.loaded:
            self.read(self.path)
            self.loaded = True


def ferengi_config(filename: str) -> ConfigProxy:
    """Returns a configuration for the respective file name."""

    return ConfigProxy(filename)
