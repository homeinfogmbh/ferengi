"""WGSI application to retrieve facebook data."""

from datetime import date, timedelta

from flask import request

from wsgilib import XML

from ferengi.facebook.client import FACEBOOK
from ferengi.facebook.functions import posts_to_dom


__all__ = ['ROUTES']


def get_posts(facebook_id):
    """Returns the respective weather forecasts."""

    days = int(request.args.get('days', 14))
    since = date.today() - timedelta(days=days)
    limit = int(request.args.get('limit', 10))
    posts = FACEBOOK.get_posts(facebook_id, since=since, limit=limit)
    return XML(posts_to_dom(posts))


ROUTES = (('GET', '/facebook/<facebook_id>', get_posts, 'get_facebook_posts'),)
