"""WGSI application to retrieve facebook data."""

from datetime import date, timedelta

from flask import request, Response
from requests import get

from wsgilib import ACCEPT, JSON, XML

from ferengi.facebook.client import Facebook
from ferengi.facebook.functions import posts_to_dom, decode_image_url


__all__ = ['ROUTES']


def get_posts(facebook_id):
    """Returns Facebook posts."""

    days = int(request.args.get('days', 14))
    since = date.today() - timedelta(days=days)
    limit = int(request.args.get('limit', 10))
    facebook = Facebook.default_instance()
    posts = facebook.get_posts(facebook_id, since=since, limit=limit)

    if 'application/xml' in ACCEPT or '*/*' in ACCEPT:
        proxy = 'proxy' in request.args
        return XML(posts_to_dom(posts, proxy=proxy))

    if 'application/json' in ACCEPT:
        return JSON([post.to_json(html=True) for post in posts])

    return ('Invalid content type.', 406)


def get_image(path):
    """Proxies images from Facebook."""

    url = request.url
    url = url.replace('%3B', ';')   # Compensate for flask's encoding.
    url = decode_image_url(url)
    response = get(url)

    if response.status_code == 200:
        mimetype = response.headers['content-type']
        return Response(response.content, mimetype=mimetype)

    return (response.text, 400)


ROUTES = (
    ('GET', '/facebook/<facebook_id>', get_posts, 'get_facebook_posts'),
    ('GET', '/facebook/image/<path:path>', get_image, 'get_facebook_image'))
