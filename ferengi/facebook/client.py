"""Facebook API client."""

from __future__ import annotations
from configparser import SectionProxy
from datetime import datetime
from os import linesep
from typing import Iterator, NamedTuple, Optional

from facebook import GraphAPI

from ferengi.facebook.config import CONFIG


__all__ = ['Facebook', 'Post']


class User(NamedTuple):
    """Facebook user information."""

    id: str
    name: str


class Post(NamedTuple):
    """A facebook post."""

    created: str
    author: str
    message: str
    image: str

    @property
    def html(self) -> str:
        """Returns the message as HTML."""
        return self.message.replace(linesep, '<br/>')

    def to_json(self, html: bool = False) -> dict:
        """Returns a JSON-ish dictionary."""
        return {
            'created': self.created,
            'author': self.author,
            'message': self.html if html else self.message,
            'image': self.image
        }


class Fields(tuple):
    """Class to represent fields selections for the graph API."""

    def __new__(cls, *items: str):
        """Returns a new tuple."""
        return super().__new__(cls, items)

    def __str__(self):
        """Returns the comma-joint items."""
        return ','.join(str(item) for item in self)

    def to_dict(self) -> dict:
        """Returns a dictionary to be used as query parameter."""
        return {'fields': str(self)}


USER_FIELDS = Fields('id', 'name')
POST_FIELDS = Fields('full_picture', 'message', 'created_time', 'from', 'type')


def _filter_links(posts: Post) -> Iterator[Post]:
    """Filters out links from posts."""

    for post in posts:
        if post['type'] != 'link':
            yield post


class Facebook(GraphAPI):
    """Extension of the facebook GraphAPI client."""

    @classmethod
    def from_id_and_secret(cls, app_id: str, app_secret: str) -> Facebook:
        """Returns a graph API client for the
        respective application id and secret.
        """
        instance = cls()
        instance.access_token = instance.get_app_access_token(
            app_id, app_secret)
        return instance

    @classmethod
    def from_config(cls, config_section: SectionProxy):
        """Returns a facebook client instance
        from the respective config section.
        """
        return cls.from_id_and_secret(
            config_section['app_id'], config_section['app_secret'])

    @classmethod
    def default_instance(cls) -> Facebook:
        """Returns the default instance."""
        return cls.from_config(CONFIG['Facebook'])

    def get_user(self, facebook_id: str, fields: Fields = USER_FIELDS) -> User:
        """Returns a user by the respective facebook ID."""
        json = self.request(f'/{facebook_id}', args=fields.to_dict())
        return User(json['id'], json['name'])

    def get_posts(self, facebook_id: str, *, limit: int = 10,
                  since: Optional[datetime] = None,
                  api_limit: Optional[int] = None,
                  fields: Fields = POST_FIELDS) -> Iterator[Post]:
        """Yields posts of the respective user."""
        args = fields.to_dict()

        if api_limit is not None:
            args['limit'] = api_limit

        if since is not None:
            args['since'] = since.strftime('%s')

        json = self.request(f'/{facebook_id}/posts', args=args)

        for count, post in enumerate(_filter_links(json['data']), start=1):
            if limit and count > limit:
                break

            message = post.get('message')

            # Skip empty messages.
            if not message:
                continue

            created = post.get('created_time')

            if created:
                created = datetime.fromisoformat(created)

            author = post.get('from', {}).get('name')
            image = post.get('full_picture')
            yield Post(created, author, message, image)
