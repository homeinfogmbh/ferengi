"""Library to store news from weltoohservice.de/xml/."""

from contextlib import suppress
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

from peewee import CharField, DateTimeField, IntegerField, TextField

from filedb import FileError, add, delete
from peeweeplus import JSONModel

from ferengi.api import get_database
from ferengi.weltnews.config import CONFIG
from ferengi.weltnews.dom import CreateFromDocument


__all__ = ['News']


DATABASE = get_database(CONFIG)
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'


class News(JSONModel):  # pylint: disable=R0902
    """News model."""

    filename = CharField(255)   # Meta information.
    subline = CharField(255)
    headline = CharField(255)
    source = CharField(255)
    textmessage = TextField()
    published = DateTimeField()
    image = IntegerField(null=True)
    thumb = IntegerField(null=True)
    video = IntegerField(null=True)
    web_url = TextField()

    @classmethod
    def from_dom(cls, news, filename):
        """Creates a new news entry from the given DOM model."""
        record = cls()
        record.filename = filename
        record.subline = news.subline
        record.headline = news.headline
        record.source = news.source
        record.textmessage = news.textmessage
        record.published = datetime.strptime(
            news.published.value(), DATETIME_FORMAT)

        if news.image.value():
            record.image = add(news.image.value())

        if news.thumb.value():
            record.thumb = add(news.thumb.value())

        if news.video.value():
            record.video = add(news.video.value())

        record.web_url = news.webUrl
        return record

    @classmethod
    def from_url(cls, url):
        """Yields records from the respective URL."""
        filename = Path(urlparse(url).path).name

        with urlopen(url) as response:
            text = response.read().decode()

        is24news = CreateFromDocument(text)

        for news in is24news.news:
            yield cls.from_dom(news, filename)

    @classmethod
    def update_from_url(cls, url):
        """Updates the records from the respective URL."""
        filename = Path(urlparse(url).path).name

        for record in cls.select().where(cls.filename == filename):
            record.delete_instance()

        for record in cls.from_url(url):
            record.save()

    def delete_instance(self, *args, **kwargs):
        """Deletes this record and related files."""
        for file in (self.image, self.thumb, self.video):
            if file is not None:
                with suppress(FileError):
                    delete(file)

        return super().delete_instance(*args, **kwargs)
