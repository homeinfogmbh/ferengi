"""API to be invoked."""

from ferengi.orm import Source


__all__ = ['update']


def update(delete_old=True):
    """Updates all sources."""

    for source in Source:
        source.update_feed(delete_old=delete_old)
