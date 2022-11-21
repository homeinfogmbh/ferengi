"""Store news from spiegel.de RSS feed in a database."""

from peeweeplus import MySQLDatabaseProxy

from ferengi.rss import RSSNews
from ferengi.googlenews.constants import RSS_FEED_URL


__all__ = ['News']


DATABASE = MySQLDatabaseProxy(
    'ferengi_googlenews',
    'ferengi.d/googlenews.conf'
)
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %z'


class News(
    RSSNews,
    rss_feed_url=RSS_FEED_URL,
    datetime_format=DATETIME_FORMAT
):
    """News model."""

    class Meta:
        database = DATABASE
        schema = database.database
