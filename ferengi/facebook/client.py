"""Facebook API client."""

from collections import namedtuple
from os import linesep

from facebook import GraphAPI

from timelib import strpdatetime

from ferengi.facebook.config import CONFIG


__all__ = ['Facebook']


User = namedtuple('FacebookUser', ('id', 'name'))


class Post:
    """A facebook post."""

    __slots__ = ('created', 'author', 'message', 'image')

    def __init__(self, created, author, message, image):
        """Creates a new post."""
        self.created = created
        self.author = author
        self.message = message
        self.image = image

    @property
    def html(self):
        """Returns the message as HTML."""
        return self.message.replace(linesep, '<br/>')

    def to_json(self, html=False):
        """Returns a JSON-ish dictionary."""
        return {
            'created': self.created,
            'author': self.author,
            'message': self.html if html else self.message,
            'image': self.image}


class Fields(tuple):
    """Class to represent fields selections for the graph API."""

    def __new__(cls, *items):
        """Returns a new tuple."""
        return super().__new__(cls, items)

    def __str__(self):
        """Returns the comma-joint items."""
        return ','.join(str(item) for item in self)

    def to_dict(self):
        """Returns a dictionary to be used as query parameter."""
        return {'fields': str(self)}


USER_FIELDS = Fields('id', 'name')
POST_FIELDS = Fields('full_picture', 'message', 'created_time', 'from', 'type')


class Facebook(GraphAPI):
    """Extension of the facebook GraphAPI client."""

    @classmethod
    def from_id_and_secret(cls, app_id, app_secret):
        """Returns a graph API client for the
        respective application id and secret.
        """
        instance = cls()
        instance.access_token = instance.get_app_access_token(
            app_id, app_secret)
        return instance

    @classmethod
    def from_config(cls, config_section):
        """Returns a facebook client instance
        from the respective config section.
        """
        return cls.from_id_and_secret(
            config_section['app_id'], config_section['app_secret'])

    @classmethod
    def default_instance(cls):
        """Returns the default instance."""
        return cls.from_config(CONFIG['Facebook'])

    def get_user(self, facebook_id, fields=USER_FIELDS):
        """Returns a user by the respective facebook ID."""
        json = self.request('/{}'.format(facebook_id), args=fields.to_dict())
        return User(json['id'], json['name'])

    def get_posts(self, facebook_id, *, limit=10, since=None,
                  fields=POST_FIELDS):
        """Yields posts of the respective user."""
        args = {'limit': limit}

        if since is not None:
            args['since'] = since.strftime('%s')

        args.update(fields.to_dict())
        json = self.request('/{}/posts'.format(facebook_id), args=args)

        for post in json['data']:
            # Skip links.
            if post['type'] == 'link':
                continue

            message = post.get('message')

            # Skip empty messages.
            if not message:
                continue

            created = post.get('created_time')

            if created:
                created = strpdatetime(created)

            author = post.get('from', {}).get('name')
            image = post.get('full_picture')
            yield Post(created, author, message, image)
