"""HTTP client."""

from ferengi.weltnews.orm import News


__all__ = ['update']


FILES = {
    'auto': False,
    'karriere': True,
    'kultur': True,
    'leute': True,
    'multimedia': True,
    'olympia2018': False,
    'panorama': True,
    'politik': True,
    'reise': True,
    'sport': True,
    'test': False,
    'wirtschaft': True,
    'wissen': True,
    'wissenschaft': True,
    'wm2018': False
}


def update() -> None:
    """Updates the records."""

    for file, active in FILES.items():
        News.update_from_file(file, active)
