"""Library to store news from weltoohservice.de/xml/."""

from __future__ import annotations
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen
from typing import Iterator

from peewee import CharField, DateTimeField, ForeignKeyField, TextField

from filedb import File
from peeweeplus import JSONModel, MySQLDatabaseProxy

from ferengi.weltnews import dom
from ferengi.weltnews.config import CONFIG
from ferengi.weltnews.functions import add_file_from_url


__all__ = ['News']


DATABASE = MySQLDatabaseProxy('ferengi_weltnews', 'ferengi.d/weltnews.conf')
DATETIME_FORMAT = '%d %b %Y %H:%M:%S %Z'


class News(JSONModel):
    """News model."""

    class Meta:
        database = DATABASE
        schema = database.database

    filename = CharField(255)   # Meta information.
    subline = CharField(255)
    headline = CharField(255)
    source = CharField(255)
    textmessage = TextField()
    published = DateTimeField()
    image = ForeignKeyField(File, column_name='image', null=True)
    thumb = ForeignKeyField(File, column_name='thumb', null=True)
    video = ForeignKeyField(File, column_name='video', null=True)
    web_url = TextField()

    @classmethod
    def from_dom(cls, news: dom.News.typeDefinition, filename: str) -> News:
        """Creates a new news entry from the given DOM model."""
        record = cls()
        record.filename = filename
        record.subline = news.subline
        record.headline = news.headline
        record.source = news.source
        record.textmessage = news.textmessage
        record.published = datetime.strptime(
            news.published.value().split(', ')[1],
            DATETIME_FORMAT
        )

        if news.image.value():
            record.image = add_file_from_url(news.image.value())

        if news.thumb.value():
            record.thumb = add_file_from_url(news.thumb.value())

        if news.video.value():
            record.video = add_file_from_url(news.video.value())

        record.web_url = news.webUrl
        return record

    @classmethod
    def from_url(cls, url: str) -> Iterator[News]:
        """Yields records from the respective URL."""
        filename = Path(urlparse(url).path).name

        with urlopen(url) as response:
            text = response.read().decode()

        is24news = dom.CreateFromDocument(text)

        for news in is24news.news:
            yield cls.from_dom(news, filename)

    @classmethod
    def update_from_url(cls, url: str, active: bool = True) -> None:
        """Updates the records from the respective URL."""
        filename = Path(urlparse(url).path).name

        for record in cls.select().where(cls.filename == filename):
            record.delete_instance()

        if active:
            for record in cls.from_url(url):
                record.save()

    @classmethod
    def update_from_file(cls, file: str, active: bool = True) -> None:
        """Updates from a news file name."""
        url = urljoin(CONFIG['api']['base_url'], f'{file}.xml')
        cls.update_from_url(url, active=active)

    def save(self, *args, **kwargs) -> int:
        """Saves the record."""
        if self.image:
            self.image.save(*args, **kwargs)

        if self.thumb:
            self.thumb.save(*args, **kwargs)

        if self.video:
            self.video.save(*args, **kwargs)

        return super().save(*args, **kwargs)
