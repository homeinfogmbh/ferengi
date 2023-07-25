"""Store news from spiegel.de RSS feed in a database."""

from __future__ import annotations

from peeweeplus import MySQLDatabaseProxy

from ferengi.spiegelnews.constants import RSS_FEED_URL

from ferengi.rss import RSSNews


__all__ = ["News"]


DATABASE = MySQLDatabaseProxy("ferengi_spiegelnews", "ferengi.d/spiegelnews.conf")
DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S %z"


class News(RSSNews, rss_feed_url=RSS_FEED_URL, datetime_format=DATETIME_FORMAT):
    """News model."""

    class Meta:
        database = DATABASE
        schema = database.database
