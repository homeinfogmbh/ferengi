"""RSS feed database."""

from datetime import datetime

from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import TextField

from ferengi.rss import dom  # pylint: disable=E0611
from ferengi.rss.config import DATABASE
from ferengi.rss.functions import strprssdatetime, strfrssdatetime


def create_tables():
    """Creates the respective tables."""

    for model in MODELS:
        model.create_table()


class RSSFeedModel(Model):
    """Base Model."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = DATABASE.database


class Source(RSSFeedModel):
    """Defines sources for the respective RSS feeds."""

    name = CharField(255)
    url = TextField()
    description = CharField(255, null=True)


class RSS(RSSFeedModel):
    """An RSS feed."""

    source = ForeignKeyField(
        Source, column_name='source', backref='feeds', on_delete='CASCADE')
    retrieved = DateTimeField(default=datetime.now)
    version = CharField(3)

    @classmethod
    def from_dom(cls, dom, source, retrieved=None):     # pylint: disable=W0621
        """Creates a new RSS feed from an XML DOM."""
        retrieved = datetime.now() if retrieved is None else retrieved
        rss = cls(source=source, retrieved=retrieved, version=dom.version)
        yield rss

        for channel in dom.channel:
            yield from Channel.from_dom(channel, rss=rss)

    def to_dom(self):
        """Returns an XML DOM."""
        rss = dom.rss()
        rss.version = self.version

        for channel in self.channels:
            rss.channel.append(channel.to_dom())

        return rss


class Channel(RSSFeedModel):
    """An RSS feed's channel."""

    rss = ForeignKeyField(
        RSS, column_name='rss', backref='channels', on_delete='CASCADE')
    title = TextField()
    link = TextField()
    description = TextField()
    language = TextField(null=True)
    copyright = TextField(null=True)
    pub_date = DateTimeField(null=True)
    last_build_date = DateTimeField(null=True)
    category = TextField(null=True)
    generator = TextField(null=True)
    ttl = IntegerField(null=True)

    @classmethod
    def from_dom(cls, dom, rss):    # pylint: disable=W0621
        """Creates a channel from an XML DOM."""
        channel = cls(
            rss=rss,
            title=dom.title,
            link=dom.link,
            description=dom.description,
            language=dom.language,
            copyright=dom.copyright,
            pub_date=strprssdatetime(dom.pubDate),
            last_build_date=strprssdatetime(dom.lastBuildDate),
            category=dom.category,
            generator=dom.generator,
            ttl=dom.ttl)
        yield channel

        for item in dom.items:
            yield Item.from_dom(item, channel=channel)

    def to_dom(self):
        """Returns an XML DOM."""
        channel = dom.Channel()
        channel.title = self.title
        channel.link = self.link
        channel.description = self.description
        channel.language = self.language
        channel.copyright = self.copyright
        channel.pubDate = strfrssdatetime(self.pub_date)
        channel.lastBuildDate = strfrssdatetime(self.lastBuildDate)
        channel.category = self.category
        channel.generator = self.generator
        channel.ttl = self.ttl

        for item in self.items:
            channel.item.append(item.to_dom())

        return channel


class Item(RSSFeedModel):
    """An RSS channel's item."""

    channel = ForeignKeyField(
        Channel, column_name='channel', backref='items', on_delete='CASCADE')
    category = TextField(null=True)
    title = TextField()
    description = TextField()
    link = TextField()
    guid = TextField(null=True)
    guid_is_permalink = BooleanField(null=True)
    pub_date = DateTimeField(null=True)

    @classmethod
    def fom_dom(cls, dom, channel):     # pylint: disable=W0621
        """Creates an item from an XML DOM."""
        return cls(
            channel=channel,
            category=dom.category,
            title=dom.title,
            description=dom.description,
            link=dom.link,
            guid=dom.guid.value(),
            guid_is_permalink=dom.guid.isPermaLink,
            pub_date=strprssdatetime(dom.pubDate)
        )

    def to_dom(self):
        """Returns an XML DOM."""
        item = dom.Item()
        item.category = self.category
        item.title = self.title
        item.description = self.description
        item.link = self.link

        if self.guid:
            item.guid = dom.GUID(self.guid, isPermaLink=self.guid_is_permalink)

        item.pubDate = strfrssdatetime(self.pub_date)
        return item


MODELS = (Source, RSS, Channel, Item)
