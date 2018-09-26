"""WGSI application to retrieve facebook data."""

from datetime import date, timedelta

from flask import request, Response
from requests import get

from wsgilib import JSON, XML, Error

from ferengi.facebook.client import FACEBOOK
from ferengi.facebook.functions import posts_to_dom, decode_image_url


__all__ = ['ROUTES']


def get_posts(facebook_id):
    """Returns Facebook posts."""

    days = int(request.args.get('days', 14))
    since = date.today() - timedelta(days=days)
    limit = int(request.args.get('limit', 10))
    posts = FACEBOOK.get_posts(facebook_id, since=since, limit=limit)

    if 'xml' in request.args:
        proxy = 'proxy' in request.args
        return XML(posts_to_dom(posts, proxy=proxy))

    return JSON([post.to_json(html=True) for post in posts])


def get_image(path):
    """Proxies images from Facebook."""

    url = decode_image_url(request.url.replace('%3B', ';'))
    response = get(url)

    if response.status_code == 200:
        return Response(response.data, mimetype=response.content_type)

    return Error(response.text)


ROUTES = (
    ('GET', '/facebook/<facebook_id>', get_posts, 'get_facebook_posts'),
    ('GET', '/facebook/image/<path:path>', get_image, 'get_facebook_image'))
