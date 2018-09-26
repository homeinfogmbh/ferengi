"""Miscellaneous functions."""

from pathlib import Path
from urllib.parse import urlparse

from ferengi.facebook import dom


__all__ = ['encode_image_url', 'decode_image_url', 'posts_to_dom']


SCHEME = 'https'
HOST = 'ferengi.homeinfo.de'
IMG_PATH = '/facebook/image'


def encode_image_url(url, path=IMG_PATH):
    """Translates URLSs to be proxied."""

    url = urlparse(url)

    if url.fragment:
        raise ValueError('Cannot encode URL with fragment.')

    params = ';{}'.format(url.params) if url.params else ''
    query = '?{}'.format(url.query) if url.query else ''
    return '{}://{}{}{}{}{}#{}'.format(
        SCHEME, HOST, path, url.path, params, query, url.netloc)


def decode_image_url(url):
    """Translates URLSs to be proxied."""

    url = urlparse(url)
    path = Path(url.path)
    parts = path.parts[2:]
    path = '/' + '/'.join(parts)
    host = url.fragment
    params = ';{}'.format(url.params) if url.params else ''
    query = '?{}'.format(url.query) if url.query else ''
    return '{}://{}{}{}{}{}'.format(
        SCHEME, host, path, url.path, params, query)


def posts_to_dom(posts, proxy=False):
    """Converts the given posts to XML dom."""

    channel = dom.channel()

    for post in posts:
        content = dom.Content()
        content.created_time = post.created
        content.from_ = post.author
        content.message = post.html

        if proxy:
            content.image = encode_image_url(post.image)
        else:
            content.image = post.image

        channel.content_.append(content)

    return channel
