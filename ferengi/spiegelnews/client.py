"""News update client."""

from feedparser import parse
from feedparser.util import FeedParserDict

from ferengi.spiegelnews.constants import RSS_FEED_URL
from ferengi.spiegelnews.orm import News


__all__ = ['update']


def update() -> None:
    """Update news from default RSS feed."""

    update_from_url(RSS_FEED_URL)


def update_from_url(url: str) -> None:
    """Create news entries from the given RSS feed URL."""

    update_from_rss(parse(url))


def update_from_rss(rss: FeedParserDict) -> None:
    """Create news entries from the given RSS feed URL."""

    update_from_entries(rss['entries'])


def update_from_entries(entries: list[FeedParserDict]) -> None:
    """Creates a new news entry from the given DOM model."""

    for article in News.select().where(True):
        article.delete_instance()

    for entry in entries:
        News.from_entry(entry).save()
