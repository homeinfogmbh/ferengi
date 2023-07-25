"""News update client."""

from logging import getLogger

from ferengi.rssapp.orm import News, Provider
from ferengi.rss import update_from_url


__all__ = ["update"]


def update() -> None:
    """Update news from default RSS feed."""

    for provider in Provider.select().where(True):
        News.delete().where(News.source == provider.url).execute()

        if provider.enabled:
            getLogger("rss.app").info("Importing news for feed: %s", provider.name)
            update_from_url(provider.url, News, clear=False)
