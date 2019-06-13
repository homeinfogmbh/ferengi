"""City name aliases."""

from functools import lru_cache
from json import load
from pathlib import Path


__all__ = ['load_aliases']


PATH = Path('/usr/local/etc/ferengi.aliases')


@lru_cache(maxsize=1)
def load_aliases(path=PATH):
    """Loads the aliases from a JSON file."""

    with path.open('r') as file:
        return load(file)
