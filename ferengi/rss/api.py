"""API to be invoked."""

from logging import getLogger

from ferengi.rss.orm import Source


__all__ = ['update']


LOGGER = getLogger('RSS')


def update(delete_old=True):
    """Updates all sources."""

    for source in Source:
        LOGGER.info('Updating source: %s.', source.name)
        source.update_feed(delete_old=delete_old)
