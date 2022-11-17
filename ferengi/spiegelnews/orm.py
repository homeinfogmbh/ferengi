"""Store news from spiegel.de RSS feed in a database."""

from __future__ import annotations
from datetime import datetime

from feedparser.util import FeedParserDict
from peewee import CharField, DateTimeField, ForeignKeyField, TextField

from filedb import File
from peeweeplus import JSONModel, MySQLDatabaseProxy

from ferengi.functions import add_file_from_url
from ferengi.spiegelnews.constants import RSS_FEED_URL


__all__ = ['News']


DATABASE = MySQLDatabaseProxy(
    'ferengi_spiegelnews',
    'ferengi.d/spiegelnews.conf'
)
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %z'


class News(JSONModel):
    """News model."""

    class Meta:
        database = DATABASE
        schema = database.database

    # Meta info
    source = TextField(default=RSS_FEED_URL)
    query_date = DateTimeField(default=datetime.now)
    # Article data
    title = TextField()
    link = TextField()
    text = TextField()
    category = CharField(255)
    image = ForeignKeyField(File, column_name='image', null=True)
    timestamp = DateTimeField()

    @classmethod
    def from_entry(cls, entry: FeedParserDict) -> News:
        """Creates a new news entry from the given DOM model."""
        record = cls()
        record.title = entry['title']
        record.link = entry['link']
        record.text = entry['summary']
        record.category = entry['category']

        for link in entry['links']:
            if link['type'].startswith('image/'):
                record.image = add_file_from_url(link['href'])
                break

        record.timestamp = datetime.strptime(
            entry['published'],
            DATETIME_FORMAT
        )
        return record

    def save(self, *args, **kwargs) -> int:
        """Save the record."""
        if self.image:
            self.image.save(*args, **kwargs)

        return super().save(*args, **kwargs)
