"""Facebook client API."""

from ferengi.facebook.client import Facebook, FACEBOOK
from ferengi.facebook.functions import posts_to_dom
from ferengi.facebook.wsgi import ROUTES


__all__ = ['FACEBOOK', 'ROUTES', 'posts_to_dom', 'Facebook']
