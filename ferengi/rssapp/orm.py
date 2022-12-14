"""Store news from spiegel.de RSS feed in a database."""

from typing import Optional

from feedparser.util import FeedParserDict
from peewee import BooleanField, CharField, TextField

from filedb import File
from peeweeplus import JSONModel, MySQLDatabaseProxy

from ferengi.functions import add_file_from_url
from ferengi.rss import RSSNews


__all__ = ['News', 'Provider']


DATABASE = MySQLDatabaseProxy(
    'ferengi_rssapp',
    'ferengi.d/rssapp.conf'
)
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


class News(
    RSSNews,
    datetime_format=DATETIME_FORMAT
):
    """News model."""

    class Meta:
        database = DATABASE
        schema = database.database

    @classmethod
    def parse_image(cls, entry: FeedParserDict) -> Optional[File]:
        """Parse an image from the entry."""
        for media_content in entry['media_content']:
            if media_content['medium'] == 'image':
                return add_file_from_url(media_content['url'])


class Provider(JSONModel):
    """News provider."""

    class Meta:
        database = DATABASE
        schema = database.database

    name = CharField(255)
    url = TextField()
    enabled = BooleanField(default=True)
