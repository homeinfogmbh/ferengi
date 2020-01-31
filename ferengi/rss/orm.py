"""RSS feed database."""

from datetime import datetime

from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import TextField
from requests import get

from ferengi.rss import dom  # pylint: disable=E0611
from ferengi.rss.config import DATABASE
from ferengi.rss.functions import strprssdatetime, strfrssdatetime


__all__ = ['MODELS', 'create_tables', 'Source', 'RSS', 'Channel', 'Item']


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

    def update_feed(self, delete_old=True):
        """Updates the RSS feed from the respective source."""
        response = get(self.url)
        xml = dom.CreateFromDocument(response.text)

        if delete_old:
            for rss in self.feeds:
                rss.delete_instance()

        for record in RSS.from_dom(xml, self, retrieved=datetime.now()):
            record.save()


class RSS(RSSFeedModel):
    """An RSS feed."""

    source = ForeignKeyField(
        Source, column_name='source', backref='feeds', on_delete='CASCADE')
    retrieved = DateTimeField(default=datetime.now)
    version = CharField(3)

    @classmethod
    def from_dom(cls, xml, source, retrieved=None):
        """Creates a new RSS feed from an XML DOM."""
        retrieved = datetime.now() if retrieved is None else retrieved
        rss = cls(source=source, retrieved=retrieved, version=xml.version)
        yield rss

        for channel in xml.channel:
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
    def from_dom(cls, xml, rss):
        """Creates a channel from an XML DOM."""
        channel = cls(
            rss=rss,
            title=xml.title,
            link=xml.link,
            description=xml.description,
            language=xml.language,
            copyright=xml.copyright,
            pub_date=strprssdatetime(xml.pubDate),
            last_build_date=strprssdatetime(xml.lastBuildDate),
            category=xml.category,
            generator=xml.generator,
            ttl=xml.ttl)
        yield channel

        for item in xml.items:
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
    def fom_dom(cls, xml, channel):
        """Creates an item from an XML DOM."""
        return cls(
            channel=channel,
            category=xml.category,
            title=xml.title,
            description=xml.description,
            link=xml.link,
            guid=xml.guid.value(),
            guid_is_permalink=xml.guid.isPermaLink,
            pub_date=strprssdatetime(xml.pubDate)
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
