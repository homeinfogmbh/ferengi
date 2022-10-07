"""HTTP client."""

from logging import getLogger
from urllib.error import HTTPError

from ferengi.weltnews.orm import News


__all__ = ['update']


FILES = {
    'auto': False,
    'infoscreen': False,
    'karriere': True,
    'kultur': True,
    'leute': True,
    'multimedia': True,
    'oohtemp': False,
    'panorama': True,
    'politik': True,
    'reise': True,
    'sport': True,
    'test': False,
    'wirtschaft': True,
    'wissen': True,
    'wissenschaft': True
}


def update() -> None:
    """Updates the records."""

    for file, active in FILES.items():
        try:
            News.update_from_file(file, active)
        except HTTPError as error:
            getLogger('weltnews').error('Could not update url: %s', error.url)
