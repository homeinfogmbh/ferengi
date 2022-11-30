"""RSS feed parsing."""

from __future__ import annotations
from datetime import datetime
from logging import getLogger
from typing import Optional, Type

from feedparser import parse
from feedparser.util import FeedParserDict
from peewee import CharField, DateTimeField, ForeignKeyField, TextField

from filedb import File
from peeweeplus import JSONModel

from ferengi.functions import add_file_from_url, extract_text


__all__ = ['RSSNews', 'update_from_url']


LOGGER = getLogger('RSS news')


class RSSNews(JSONModel):
    """Abstract model to store news from RSS feeds."""

    # Meta info
    source = TextField()
    query_date = DateTimeField(default=datetime.now)
    # Article data
    title = TextField()
    link = TextField()
    text = TextField()
    category = CharField(255, null=True)
    author = CharField(255, null=True)
    image = ForeignKeyField(File, column_name='image', null=True)
    published = DateTimeField()

    def __init_subclass__(
            cls,
            *args,
            rss_feed_url: str | None = None,
            datetime_format: str = '%a, %d %b %Y %H:%M:%S %z',
            **kwargs
    ):
        super().__init_subclass__(*args, **kwargs)
        cls.source.default = rss_feed_url
        cls.DATETIME_FORMAT = datetime_format

    @classmethod
    def parse_image(cls, entry: FeedParserDict) -> Optional[File]:
        """Parse an image from the entry."""
        for link in entry['links']:
            if link['type'].startswith('image/'):
                return add_file_from_url(link['href'])

    @classmethod
    def from_entry(cls, entry: FeedParserDict, **kwargs) -> RSSNews:
        """Creates a new news entry from the given DOM model."""
        record = cls(**kwargs)
        record.title = entry['title']
        record.link = entry['link']

        if (text := extract_text(entry['summary'])) is None:
            raise ValueError('No article text.')

        record.text = text
        record.category = entry.get('category')
        record.author = entry.get('author')
        record.image = cls.parse_image(entry)
        record.published = datetime.strptime(
            entry['published'],
            cls.DATETIME_FORMAT
        )
        return record

    def save(self, *args, **kwargs) -> int:
        """Save the record."""
        if self.image:
            self.image.save(*args, **kwargs)

        return super().save(*args, **kwargs)


def update_from_url(url: str, model: Type[RSSNews], **kwargs) -> None:
    """Create news entries from the given RSS feed URL."""

    update_from_rss(parse(url), model, **kwargs)


def update_from_rss(
        rss: FeedParserDict,
        model: Type[RSSNews],
        **kwargs
) -> None:
    """Create news entries from the given RSS feed URL."""

    update_from_entries(rss['entries'], model, **kwargs)


def update_from_entries(
        entries: list[FeedParserDict],
        model: Type[RSSNews],
        **kwargs
) -> None:
    """Creates a new news entry from the given DOM model."""

    for article in model.select().where(True):
        article.delete_instance()

    count = errors = 0

    for count, entry in enumerate(entries, start=1):
        try:
            news = model.from_entry(entry, **kwargs)
        except (KeyError, ValueError) as error:
            errors += 1
            LOGGER.error('Could not update news entry: %s', error)
        else:
            news.save()

    LOGGER.info('Updated %i / %i entries', count - errors, count)
