"""Facebook API client."""

from collections import namedtuple
from os import linesep

from facebook import GraphAPI

from timelib import strpdatetime

from ferengi.facebook.config import CONFIG


__all__ = ['Facebook']


User = namedtuple('FacebookUser', ('id', 'name'))


class Post(namedtuple('FacebookPost', 'created author message image')):
    """A facebook post."""

    __slots__ = ()

    @property
    def html(self):
        """Returns the message as HTML."""
        return self.message.replace(linesep, '<br/>')


class Facebook(GraphAPI):
    """Extension of the facebook grapth API client."""

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

    def get_user(self, facebook_id):
        """Returns a user by the respective facebook ID."""
        fields = ('id', 'name')
        args = {'fields': ','.join(fields)}
        dictionary = self.request('/{}'.format(facebook_id), args=args)
        return User(dictionary['id'], dictionary['name'])

    def get_posts(self, facebook_id, *, limit=10, since=None):
        """Yields posts of the respective user."""
        fields = ('full_picture', 'message', 'created_time', 'from', 'type')
        args = {'fields': ','.join(fields), 'limit': limit}

        if since is not None:
            args['since'] = since.strftime('%s')

        dictionary = self.request('/{}/posts'.format(facebook_id), args=args)

        for post in dictionary['data']:
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


FACEBOOK = Facebook.from_config(CONFIG['Facebook'])
