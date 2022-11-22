"""Store news from spiegel.de RSS feed in a database."""

from typing import Optional

from feedparser.util import FeedParserDict

from filedb import File
from peeweeplus import MySQLDatabaseProxy

from ferengi.functions import add_file_from_url
from ferengi.rss import RSSNews
from ferengi.googlenews.constants import RSS_FEED_URL


__all__ = ['News']


DATABASE = MySQLDatabaseProxy(
    'ferengi_googlenews',
    'ferengi.d/googlenews.conf'
)
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


class News(
    RSSNews,
    rss_feed_url=RSS_FEED_URL,
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
